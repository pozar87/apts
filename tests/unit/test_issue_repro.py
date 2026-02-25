import pytest
from apts.equipment import Equipment
from apts.constants import GraphConstants
import matplotlib.colors as mcolors


def test_plot_connection_graph_background_color():
    eq = Equipment()
    # Test dark mode override
    res = eq.plot_connection_graph(dark_mode_override=True)
    fig = res.fig

    expected_facecolor_hex = GraphConstants.DARK_MODE_STYLE["FIGURE_FACE_COLOR"]
    expected_rgba = mcolors.to_rgba(expected_facecolor_hex)

    # Matplotlib might return slightly different float precision, so we use approx or compare closely
    actual_rgba = fig.get_facecolor()
    assert actual_rgba == pytest.approx(expected_rgba), (
        f"Expected {expected_rgba}, got {actual_rgba}"
    )

    # Test light mode override
    res_light = eq.plot_connection_graph(dark_mode_override=False)
    fig_light = res_light.fig
    expected_facecolor_hex_light = GraphConstants.LIGHT_MODE_STYLE["FIGURE_FACE_COLOR"]
    expected_rgba_light = mcolors.to_rgba(expected_facecolor_hex_light)
    actual_rgba_light = fig_light.get_facecolor()
    assert actual_rgba_light == pytest.approx(expected_rgba_light), (
        f"Expected {expected_rgba_light}, got {actual_rgba_light}"
    )


def test_plot_connection_graph_svg_contains_color():
    eq = Equipment()
    svg_data = eq.plot_connection_graph_svg(dark_mode_override=True)

    expected_facecolor_hex = GraphConstants.DARK_MODE_STYLE["FIGURE_FACE_COLOR"].lower()
    assert expected_facecolor_hex in svg_data.lower(), (
        f"SVG should contain {expected_facecolor_hex}"
    )

    # Ensure it doesn't have white background if it's supposed to be dark
    # Matplotlib SVG uses <rect ... fill="#ffffff"/> for white background
    # But it might also use rgb(100%,100%,100%)
    assert 'fill="#ffffff"' not in svg_data.lower()
