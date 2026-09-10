from datetime import datetime, timezone

import matplotlib.figure
import pytest

from apts.events import Event
from apts.visualization import plot_finder_chart


@pytest.fixture
def sample_occultation_event():
    return Event(
        category="OCCULTATION",
        title="Lunar occultation of Jupiter",
        datetime_utc=datetime(2026, 9, 8, 5, 50, tzinfo=timezone.utc),
        best_viewing_time_local="05:50",
        location_name="Chicago",
        description="The Moon will pass in front of Jupiter.",
        angular_separation="10.3°",
        azimuth_deg=90.0,
        altitude_deg=25.0,
        objects=["Moon", "Jupiter"],
    )


def test_generate_finder_chart_png(sample_occultation_event):
    png_bytes = sample_occultation_event.generate_finder_chart(format="png", theme="stargazer_dark")
    assert isinstance(png_bytes, bytes)
    assert len(png_bytes) > 0
    # PNG signature check: \x89PNG
    assert png_bytes[:4] == b"\x89PNG"


def test_generate_finder_chart_svg(sample_occultation_event):
    svg_out = sample_occultation_event.generate_finder_chart(format="svg", theme="stargazer_dark")
    assert isinstance(svg_out, str)
    assert "<svg" in svg_out.lower()


def test_generate_finder_chart_figure(sample_occultation_event):
    fig = plot_finder_chart(sample_occultation_event, format="figure", theme="stargazer_dark")
    assert isinstance(fig, matplotlib.figure.Figure)
    assert len(fig.axes) == 1


def test_generate_finder_chart_light_theme(sample_occultation_event):
    png_bytes = sample_occultation_event.generate_finder_chart(format="png", theme="stargazer_light")
    assert isinstance(png_bytes, bytes)
    assert len(png_bytes) > 0


def test_rocket_launch_chart_rendering():
    launch_event = Event(
        category="ROCKET_LAUNCH",
        title="Falcon 9 Rocket Launch",
        datetime_utc=datetime(2026, 9, 8, 12, 0, tzinfo=timezone.utc),
        best_viewing_time_local="12:00",
        location_name="Cape Canaveral",
    )
    png_bytes = launch_event.generate_finder_chart(format="png")
    assert isinstance(png_bytes, bytes)
    assert len(png_bytes) > 0
    assert png_bytes[:4] == b"\x89PNG"

    fig = plot_finder_chart(launch_event, format="figure")
    assert isinstance(fig, matplotlib.figure.Figure)


def test_iss_flyby_chart_rendering():
    flyby_event = Event(
        category="FLYBY",
        title="Bright ISS Pass",
        datetime_utc=datetime(2026, 9, 8, 22, 15, tzinfo=timezone.utc),
        best_viewing_time_local="22:15",
        location_name="Berlin",
        azimuth_deg=140.0,
        altitude_deg=45.0,
        objects=["ISS"],
    )
    png_bytes = flyby_event.generate_finder_chart(format="png")
    assert isinstance(png_bytes, bytes)
    assert len(png_bytes) > 0
    assert png_bytes[:4] == b"\x89PNG"


def test_meteor_shower_chart_rendering():
    shower_event = Event(
        category="METEOR_SHOWER",
        title="Perseids Meteor Shower Peak",
        datetime_utc=datetime(2026, 8, 12, 2, 0, tzinfo=timezone.utc),
        best_viewing_time_local="02:00",
        location_name="Warsaw",
        azimuth_deg=45.0,
        altitude_deg=50.0,
        objects=["Perseids"],
    )
    png_bytes = shower_event.generate_finder_chart(format="png")
    assert isinstance(png_bytes, bytes)
    assert len(png_bytes) > 0


def test_jovian_moon_event_chart_rendering():
    jovian_event = Event(
        category="JOVIAN_MOON_EVENT",
        title="Io Shadow Transit on Jupiter",
        datetime_utc=datetime(2026, 9, 8, 1, 30, tzinfo=timezone.utc),
        best_viewing_time_local="01:30",
        location_name="Madrid",
        azimuth_deg=180.0,
        altitude_deg=35.0,
        objects=["Jupiter", "Io"],
    )
    png_bytes = jovian_event.generate_finder_chart(format="png")
    assert isinstance(png_bytes, bytes)
    assert len(png_bytes) > 0


def test_planet_alignment_chart_rendering():
    alignment_event = Event(
        category="PLANET_ALIGNMENT",
        title="Planetary Alignment of Venus, Mars, and Jupiter",
        datetime_utc=datetime(2026, 9, 8, 4, 30, tzinfo=timezone.utc),
        best_viewing_time_local="04:30",
        location_name="Lisbon",
        azimuth_deg=105.0,
        altitude_deg=20.0,
        objects=["Venus", "Mars", "Jupiter"],
    )
    png_bytes = alignment_event.generate_finder_chart(format="png")
    assert isinstance(png_bytes, bytes)
    assert len(png_bytes) > 0


def test_east_conjunction_azimuth_alignment():
    east_event = Event(
        category="CONJUNCTION",
        title="Conjunction of Moon and Jupiter",
        datetime_utc=datetime(2026, 9, 8, 5, 0, tzinfo=timezone.utc),
        best_viewing_time_local="05:00",
        location_name="Warsaw",
        azimuth_deg=108.5,
        altitude_deg=22.0,
        objects=["Moon", "Jupiter"],
    )
    fig = plot_finder_chart(east_event, format="figure")
    ax = fig.axes[0]
    xlim = ax.get_xlim()
    center_az = (xlim[0] + xlim[1]) / 2.0
    # Chart should be centered near 108.5° azimuth, NOT forced to 90.0°
    assert abs(center_az - 108.5) < 5.0


def test_sky_brightness_metadata_and_durations(sample_occultation_event):
    d = sample_occultation_event.to_dict()
    assert "sky_brightness" in d
    assert d["sky_brightness"] in (
        "DAY",
        "CIVIL_TWILIGHT",
        "NAUTICAL_TWILIGHT",
        "ASTRONOMICAL_TWILIGHT",
        "NIGHT_MOONLIT",
        "NIGHT_DARK",
    )

    from apts.events.calculations.evaluations import calculate_event_duration

    conj_duration = calculate_event_duration("Conjunction", {})
    assert conj_duration == 7200  # 2 hours
