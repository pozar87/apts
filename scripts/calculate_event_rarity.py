import argparse
import datetime
import json
import logging
import os
import sys
import time
from concurrent.futures import ProcessPoolExecutor, as_completed

import pandas as pd

# Add the project root to sys.path to import apts
sys.path.append(os.getcwd())

from apts.constants.event_types import EventType
from apts.events import AstronomicalEvents
from apts.place import Place

# Configure logging
logging.basicConfig(
    level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Events that CAN be simulated over long periods (purely astronomical)
EVENTS_TO_SIMULATE = [
    EventType.MOON_PHASES,
    EventType.CONJUNCTIONS,
    EventType.OPPOSITIONS,
    EventType.METEOR_SHOWERS,
    EventType.HIGHEST_ALTITUDES,
    EventType.LUNAR_OCCULTATIONS,
    EventType.APHELION_PERIHELION,
    EventType.MOON_APOGEE_PERIGEE,
    EventType.MERCURY_INFERIOR_CONJUNCTIONS,
    EventType.MOON_MESSIER_CONJUNCTIONS,
    EventType.SOLAR_ECLIPSES,
    EventType.LUNAR_ECLIPSES,
    EventType.MOON_STAR_CONJUNCTIONS,
    EventType.PLANET_ALIGNMENTS,
]

# Diverse locations to get a global average
LOCATIONS = [
    {"name": "Warsaw", "lat": 52.2297, "lon": 21.0122},
    {"name": "Sydney", "lat": -33.8688, "lon": 151.2093},
    {"name": "Quito", "lat": -0.1807, "lon": -78.4678},
    {"name": "Tromso", "lat": 69.6492, "lon": 18.9553},
    {"name": "Punta Arenas", "lat": -53.1638, "lon": -70.9171},
]


def simulate_chunk(loc_config, chunk_start_year, chunk_end_year):
    """Simulates a chunk of years for a specific location."""
    try:
        place = Place(loc_config["lat"], loc_config["lon"], name=loc_config["name"])
        chunk_start_date = datetime.datetime(
            chunk_start_year, 1, 1, tzinfo=datetime.timezone.utc
        )
        chunk_end_date = datetime.datetime(
            chunk_end_year, 1, 1, tzinfo=datetime.timezone.utc
        )

        ae = AstronomicalEvents(
            place,
            chunk_start_date,
            chunk_end_date,
            events_to_calculate=EVENTS_TO_SIMULATE,
        )
        events_df = ae.get_events()
        ae.shutdown()

        if not events_df.empty:
            # Keep only necessary columns for stats to save memory
            cols_to_keep = [
                "type",
                "event",
                "separation_degrees",
                "object",
                "object1",
                "object2",
                "planets",
                "eclipse_kind",
                "is_transit",
                "altitude",
            ]
            existing_cols = [c for c in cols_to_keep if c in events_df.columns]
            return events_df[existing_cols]
    except Exception as e:
        logger.error(
            f"Error in {loc_config['name']} ({chunk_start_year}-{chunk_end_year}): {e}"
        )
    return pd.DataFrame()


def print_progress(iteration, total, prefix="", suffix="", length=50):
    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = "█" * filled_length + "-" * (length - filled_length)
    print(
        f"\r{prefix} |{bar}| {iteration}/{total} ({percent}%) {suffix}",
        end="",
        flush=True,
    )


def main():
    parser = argparse.ArgumentParser(description="Calculate event rarity statistics.")
    parser.add_argument(
        "--years",
        type=int,
        default=50,
        help="Number of years to simulate per location (default: 50)",
    )
    parser.add_argument(
        "--workers",
        type=int,
        default=2,
        help="Number of parallel processes (default: 2)",
    )
    parser.add_argument(
        "--chunk-size", type=int, default=5, help="Years per task (default: 5)"
    )
    parser.add_argument(
        "--start-year", type=int, default=2024, help="Starting year (default: 2024)"
    )
    args = parser.parse_args()

    total_years = args.years
    max_workers = args.workers
    chunk_size = args.chunk_size
    start_year = args.start_year

    print("Configuration:")
    print(f"  Total years: {total_years}")
    print(f"  Locations:   {len(LOCATIONS)}")
    print(f"  Parallelism: {max_workers} workers")
    print(f"  Chunk size:  {chunk_size} years")

    tasks = []
    for loc in LOCATIONS:
        for cy in range(start_year, start_year + total_years, chunk_size):
            end_y = min(cy + chunk_size, start_year + total_years)
            tasks.append((loc, cy, end_y))

    total_tasks = len(tasks)
    completed_tasks = 0
    all_results = []

    print(f"\nProcessing {total_tasks} tasks...")
    start_time = time.time()

    # Using a limited number of workers to prevent OOM on some systems
    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        futures = {
            executor.submit(simulate_chunk, loc, s, e): (loc["name"], s)
            for loc, s, e in tasks
        }

        for future in as_completed(futures):
            completed_tasks += 1
            loc_name, s_year = futures[future]
            df = future.result()
            if df is not None and not df.empty:
                all_results.append(df)

            elapsed = time.time() - start_time
            print_progress(
                completed_tasks,
                total_tasks,
                prefix="Progress:",
                suffix=f"[{loc_name} {s_year}] {elapsed:.1f}s",
            )

    if not all_results:
        print("\n\nNo results obtained. Check logs for errors.")
        return

    print("\n\nAggregating results and calculating statistics...")
    full_df = pd.concat(all_results, ignore_index=True)

    # Free up memory
    del all_results

    total_obs_years = total_years * len(LOCATIONS)

    stats = {
        "metadata": {
            "total_years_simulated": total_years,
            "locations_count": len(LOCATIONS),
            "total_observation_years": total_obs_years,
            "start_year": start_year,
            "generated_at": datetime.datetime.now().isoformat(),
        },
        "frequencies": {},
        "thresholds": {},
    }

    event_types = full_df["type"].unique()

    for etype in event_types:
        type_df = full_df[full_df["type"] == etype]
        count = len(type_df)
        freq = count / total_obs_years
        stats["frequencies"][etype] = freq

        # Calculate thresholds for separation-based events
        if etype in [
            "Conjunction",
            "Moon-Messier Conjunction",
            "Moon-Star Conjunction",
        ]:
            seps = pd.Series(type_df["separation_degrees"]).dropna()
            if not seps.empty:
                # Rarity 5 (top 2%), 4 (top 10%), 3 (top 30%), 2 (top 60%)
                stats["thresholds"][etype] = {
                    "r5": float(seps.quantile(0.02)),
                    "r4": float(seps.quantile(0.10)),
                    "r3": float(seps.quantile(0.30)),
                    "r2": float(seps.quantile(0.60)),
                }

        if etype == "Planet Alignment":
            # Extract number of planets from event string if needed,
            # or use planets column if it's a list
            def get_p_count(row):
                if isinstance(row.get("planets"), list):
                    return len(row["planets"])
                import re

                match = re.search(r"(\d+)", str(row.get("event", "")))
                return int(match.group(1)) if match else 0

            p_counts = type_df.apply(get_p_count, axis=1).value_counts().to_dict()
            stats["thresholds"][etype] = {
                str(int(k)): v / total_obs_years for k, v in p_counts.items()
            }

        if etype == "Lunar Eclipse":
            kinds = pd.Series(type_df["eclipse_kind"]).value_counts().to_dict()
            stats["thresholds"][etype] = {
                str(k): v / total_obs_years for k, v in kinds.items()
            }

    # Save results
    output_file = "event_rarity_stats.json"
    with open(output_file, "w") as f:
        json.dump(stats, f, indent=2)

    print(f"Statistics saved to {output_file}")

    print("\nSimulation Summary (Events per Year):")
    for etype, freq in sorted(stats["frequencies"].items(), key=lambda x: x[1]):
        print(f"  {etype:30}: {freq:.4f}")


if __name__ == "__main__":
    main()
