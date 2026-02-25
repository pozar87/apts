from datetime import datetime, timezone
from apts import Equipment, Observation, Place
from apts.cache import clear_cache
from apts.i18n import language_context


def test_german_translation_for_plots():
    """
    Tests that the language of plots can be switched to German.
    """
    clear_cache()
    my_place = Place(
        lat=52.5200,
        lon=13.4050,
        name="Berlin",
        date=datetime(2025, 1, 1, tzinfo=timezone.utc),
    )
    equipment = Equipment()
    observation = Observation(place=my_place, equipment=equipment)

    with language_context("de"):
        fig_de = observation.plot_messier()
        assert fig_de is not None
        assert fig_de.axes[0].get_title() == "Höhe der Messier-Objekte"


def test_german_translation_for_constellations():
    """
    Tests that the constellations are translated to German.
    """
    clear_cache()
    target_date = datetime(2025, 1, 1, tzinfo=timezone.utc)
    my_place = Place(lat=52.5200, lon=13.4050, name="Berlin")  # Berlin
    equipment = Equipment()

    observation = Observation(
        place=my_place,
        equipment=equipment,
        target_date=target_date,
    )

    visible_messier_de = observation.get_visible_messier(language="de")
    # Auriga should be translated to Fuhrmann
    assert "Fuhrmann" in visible_messier_de["Constellation"].values
    # Spiral Galaxy should be translated to Spiralgalaxie
    assert "Spiralgalaxie" in visible_messier_de["Type"].values
