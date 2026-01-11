#!/usr/bin/env python3
"""
Performance Analysis Utility for APTS

This module provides utilities for analyzing performance bottlenecks
in astronomical calculations and tests.
"""

import time
import functools
import cProfile
import pstats
import io
from contextlib import contextmanager
from typing import Dict, List, Callable, Optional
import pandas as pd
from datetime import datetime


class PerformanceProfiler:
    """A comprehensive performance profiler for APTS operations."""

    def __init__(self):
        self.timings: Dict[str, List[float]] = {}
        self.memory_usage: Dict[str, List[float]] = {}
        self.call_counts: Dict[str, int] = {}
        self.start_times: Dict[str, float] = {}

    def time_function(self, name: Optional[str] = None):
        """Decorator to time function execution."""

        def decorator(func: Callable) -> Callable:
            func_name = name or f"{func.__module__}.{func.__name__}"

            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                start_time = time.perf_counter()
                start_memory = self._get_memory_usage()

                try:
                    result = func(*args, **kwargs)
                    return result
                finally:
                    end_time = time.perf_counter()
                    end_memory = self._get_memory_usage()

                    execution_time = end_time - start_time
                    memory_delta = end_memory - start_memory

                    if func_name not in self.timings:
                        self.timings[func_name] = []
                        self.memory_usage[func_name] = []
                        self.call_counts[func_name] = 0

                    self.timings[func_name].append(execution_time)
                    self.memory_usage[func_name].append(memory_delta)
                    self.call_counts[func_name] += 1

            return wrapper

        return decorator

    @contextmanager
    def time_block(self, block_name: str):
        """Context manager to time a block of code."""
        start_time = time.perf_counter()
        start_memory = self._get_memory_usage()
        self.start_times[block_name] = start_time

        try:
            yield
        finally:
            end_time = time.perf_counter()
            end_memory = self._get_memory_usage()

            execution_time = end_time - start_time
            memory_delta = end_memory - start_memory

            if block_name not in self.timings:
                self.timings[block_name] = []
                self.memory_usage[block_name] = []
                self.call_counts[block_name] = 0

            self.timings[block_name].append(execution_time)
            self.memory_usage[block_name].append(memory_delta)
            self.call_counts[block_name] += 1

    def _get_memory_usage(self) -> float:
        """Get current memory usage in MB (simplified version)."""
        # Simplified memory tracking - returns 0 as placeholder
        # For detailed memory analysis, install psutil: pip install psutil
        return 0.0

    def get_summary(self) -> pd.DataFrame:
        """Get a summary of all timed operations."""
        summary_data = []

        for name in self.timings.keys():
            times = self.timings[name]
            memory_deltas = self.memory_usage[name]

            summary_data.append(
                {
                    "Operation": name,
                    "Call Count": self.call_counts[name],
                    "Total Time (s)": sum(times),
                    "Average Time (s)": sum(times) / len(times),
                    "Min Time (s)": min(times),
                    "Max Time (s)": max(times),
                    "Average Memory Delta (MB)": sum(memory_deltas)
                    / len(memory_deltas),
                    "Max Memory Delta (MB)": max(memory_deltas) if memory_deltas else 0,
                }
            )

        df = pd.DataFrame(summary_data)
        return df.sort_values("Total Time (s)", ascending=False)

    def print_summary(self, top_n: int = 20):
        """Print a formatted summary of performance data."""
        summary = self.get_summary()

        print("\n" + "=" * 80)
        print("APTS PERFORMANCE ANALYSIS SUMMARY")
        print("=" * 80)
        print(f"Analysis Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Total Operations Tracked: {len(summary)}")
        print(f"Total Execution Time: {summary['Total Time (s)'].sum():.2f}s")
        print(f"Current Process Memory: {self._get_memory_usage():.2f} MB (simplified)")
        print("\n" + "-" * 80)
        print("TOP SLOWEST OPERATIONS:")
        print("-" * 80)

        for i, row in summary.head(top_n).iterrows():
            print(
                f"{row['Operation']:<50} "
                f"{row['Total Time (s)']:>8.3f}s "
                f"({row['Call Count']:>3} calls, "
                f"avg: {row['Average Time (s)']:>6.3f}s)"
            )

        print("\n" + "-" * 80)
        print("MEMORY INTENSIVE OPERATIONS:")
        print("-" * 80)

        memory_summary = summary.sort_values("Max Memory Delta (MB)", ascending=False)
        for i, row in memory_summary.head(10).iterrows():
            if row["Max Memory Delta (MB)"] > 0:
                print(
                    f"{row['Operation']:<50} "
                    f"{row['Max Memory Delta (MB)']:>8.2f} MB "
                    f"(avg: {row['Average Memory Delta (MB)']:>6.2f} MB) "
                    f"[Note: Install psutil for accurate memory tracking]"
                )

    def reset(self):
        """Reset all collected performance data."""
        self.timings.clear()
        self.memory_usage.clear()
        self.call_counts.clear()
        self.start_times.clear()


class TestPerformanceAnalyzer:
    """Specialized analyzer for pytest test performance."""

    def __init__(self):
        self.test_times: Dict[str, float] = {}
        self.setup_times: Dict[str, float] = {}
        self.teardown_times: Dict[str, float] = {}

    def analyze_pytest_output(self, durations_output: str) -> pd.DataFrame:
        """Parse pytest --durations output and return analysis."""
        lines = durations_output.strip().split("\n")
        test_data = []

        parsing_durations = False
        for line in lines:
            if "slowest" in line.lower() and "durations" in line.lower():
                parsing_durations = True
                continue

            if parsing_durations and line.startswith("="):
                break

            if parsing_durations and "s call" in line:
                parts = line.split()
                if len(parts) >= 3:
                    duration = float(parts[0].replace("s", ""))
                    test_name = parts[2] if len(parts) > 2 else "unknown"
                    test_data.append(
                        {"Test": test_name, "Duration (s)": duration, "Type": "call"}
                    )

        return pd.DataFrame(test_data)

    def suggest_optimizations(self, df: pd.DataFrame) -> List[str]:
        """Suggest optimizations based on test performance data."""
        suggestions = []

        slow_tests = df[df["Duration (s)"] > 5.0]
        if not slow_tests.empty:
            suggestions.append(
                f"Consider optimizing {len(slow_tests)} tests taking >5s each"
            )

        cache_related = df[
            df["Test"].str.contains("cache|pickle", case=False, na=False)
        ]
        if not cache_related.empty and cache_related["Duration (s)"].mean() > 2:
            suggestions.append(
                "Cache-related tests are slow - consider session-scoped caching"
            )

        solar_tests = df[df["Test"].str.contains("solar|planet", case=False, na=False)]
        if not solar_tests.empty and solar_tests["Duration (s)"].mean() > 3:
            suggestions.append(
                "Solar/planetary tests are slow - consider limiting MPCORB data loading"
            )

        return suggestions


def profile_function(func: Callable, *args, **kwargs) -> tuple:
    """Profile a single function call and return results and stats."""
    profiler = cProfile.Profile()
    profiler.enable()

    start_time = time.perf_counter()
    result = func(*args, **kwargs)
    end_time = time.perf_counter()

    profiler.disable()

    # Capture profile stats
    stats_buffer = io.StringIO()
    stats = pstats.Stats(profiler, stream=stats_buffer)
    stats.sort_stats("cumulative")
    stats.print_stats(20)  # Top 20 functions

    return result, stats_buffer.getvalue(), end_time - start_time


def benchmark_astronomical_operations():
    """Benchmark common astronomical operations in APTS."""
    from apts.place import Place
    from apts.objects.solar_objects import SolarObjects
    from apts.objects.messier import Messier
    from apts.catalogs import Catalogs

    profiler = PerformanceProfiler()

    print("Benchmarking APTS astronomical operations...")

    # Benchmark Place creation
    with profiler.time_block("place_creation"):
        place = Place(lat=52.2, lon=21.0, name="Warsaw")

    # Benchmark SolarObjects creation and computation
    with profiler.time_block("solar_objects_init"):
        solar_objects = SolarObjects(place)

    with profiler.time_block("solar_objects_compute"):
        solar_objects.compute()

    # Benchmark Messier objects
    with profiler.time_block("messier_init"):
        messier = Messier(place, Catalogs())

    with profiler.time_block("messier_compute"):
        messier.compute()

    # Print results
    profiler.print_summary()

    return profiler


def analyze_cache_performance():
    """Analyze the performance impact of caching strategies."""
    from apts.cache import get_mpcorb_data, get_ephemeris, get_timescale

    profiler = PerformanceProfiler()

    print("Analyzing cache performance...")

    # Test cold cache performance
    print("Testing cold cache...")
    get_mpcorb_data.cache_clear()
    get_ephemeris.cache_clear()
    get_timescale.cache_clear()

    with profiler.time_block("cold_cache_mpcorb"):
        get_mpcorb_data()

    with profiler.time_block("cold_cache_ephemeris"):
        get_ephemeris()

    with profiler.time_block("cold_cache_timescale"):
        get_timescale()

    # Test warm cache performance
    print("Testing warm cache...")
    for i in range(5):
        with profiler.time_block(f"warm_cache_mpcorb_{i}"):
            get_mpcorb_data()

        with profiler.time_block(f"warm_cache_ephemeris_{i}"):
            get_ephemeris()

        with profiler.time_block(f"warm_cache_timescale_{i}"):
            get_timescale()

    profiler.print_summary()
    return profiler


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        if sys.argv[1] == "benchmark":
            benchmark_astronomical_operations()
        elif sys.argv[1] == "cache":
            analyze_cache_performance()
        elif sys.argv[1] == "test-analysis" and len(sys.argv) > 2:
            analyzer = TestPerformanceAnalyzer()
            with open(sys.argv[2], "r") as f:
                output = f.read()
            df = analyzer.analyze_pytest_output(output)
            print(df)
            suggestions = analyzer.suggest_optimizations(df)
            print("\nOptimization Suggestions:")
            for suggestion in suggestions:
                print(f"- {suggestion}")
        else:
            print(
                "Usage: python performance_analysis.py [benchmark|cache|test-analysis <file>]"
            )
    else:
        print("Running full benchmark...")
        benchmark_astronomical_operations()
