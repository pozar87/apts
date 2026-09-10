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
