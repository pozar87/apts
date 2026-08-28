import pandas as pd
from typing import cast
from apts.catalogs import Catalogs
from apts.constants import ObjectTableLabels
from apts.constants.objecttablelabels import TECHNICAL_COLUMNS


def test_messier_catalog():
    c = cast(pd.DataFrame, Catalogs().MESSIER)
    # Messier catalog contains 110 objects
    assert len(c) == 110
    # M13 is  Hercules Globular Cluster - NGC 6205 (index starts from 0)
    assert c.iloc[12]["NGC"] == "NGC 6205"
    assert c.iloc[12]["Name"] == "Hercules Globular Cluster"
    # M45 is Pleiades (index starts from 0)
    assert c.iloc[44]["Messier"] == "M45"
    assert "Pleiades" in c.iloc[44]["Name"]
    # M82 is Cigar Galaxy - NGC 3034 (index starts from 0)
    assert c.iloc[81]["NGC"] == "NGC 3034"
    assert c.iloc[81]["Name"] == "Cigar Galaxy"
    # Andromeda is the biggest galaxy
    # Sort using magnitude value of Size Major
    largest_objects = c.sort_values(
        by=ObjectTableLabels.SIZE_MAJOR,
        key=lambda x: cast(pd.Series, x.apply(lambda y: getattr(y, "magnitude", y))),
        ascending=False,
    )
    assert largest_objects.iloc[0]["Name"] == "Andromeda Galaxy"
    assert largest_objects.iloc[0]["Messier"] == "M31"
    assert largest_objects.iloc[0]["NGC"] == "NGC 224"
    # Check data types
    # String columns should have 'string' dtype
    assert c["Messier"].dtype == "string"
    assert c["NGC"].dtype == "string"
    assert c["Name"].dtype == "string"
    assert c["Type"].dtype == "string"
    assert c["Constellation"].dtype == "string"

    # Unit columns should have attributes of pint.Quantity
    assert hasattr(c["RA"].iloc[0], "magnitude")
    assert hasattr(c["RA"].iloc[0], "units")
    assert c["RA"].iloc[0].units == "hour"

    assert hasattr(c["Dec"].iloc[0], "magnitude")
    assert hasattr(c["Dec"].iloc[0], "units")
    assert c["Dec"].iloc[0].units == "degree"

    assert hasattr(c["Distance"].iloc[0], "magnitude")
    assert hasattr(c["Distance"].iloc[0], "units")
    assert str(c["Distance"].iloc[0].units) == "light_year"

    assert hasattr(c[ObjectTableLabels.SIZE_MAJOR].iloc[0], "magnitude")
    assert hasattr(c[ObjectTableLabels.SIZE_MAJOR].iloc[0], "units")
    assert c[ObjectTableLabels.SIZE_MAJOR].iloc[0].units == "arcminute"

    assert hasattr(c["Magnitude"].iloc[0], "magnitude")
    assert hasattr(c["Magnitude"].iloc[0], "units")
    assert c["Magnitude"].iloc[0].units == "mag"

    # Check external links
    assert "SIMBAD" in c.columns
    assert "ALADIN" in c.columns
    assert "Astrobin" in c.columns
    assert c.iloc[0]["SIMBAD"].startswith(
        "https://simbad.u-strasbg.fr/simbad/sim-basic?Ident=M1"
    )
    assert c.iloc[0]["ALADIN"].startswith(
        "https://aladin.cds.unistra.fr/AladinLite/?target=M1"
    )
    assert c.iloc[0]["Astrobin"].startswith("https://www.astrobin.com/search/?q=M1")


def test_ngc_catalog():
    c = cast(pd.DataFrame, Catalogs().NGC)
    # Check if some objects are loaded
    assert len(c) > 0

    # Check external links
    assert "SIMBAD" in c.columns
    assert "ALADIN" in c.columns
    assert "Astrobin" in c.columns

    # Check specific object, e.g., IC0001
    ic1 = c[c["Name"] == "IC0001"].iloc[0]
    assert ic1["SIMBAD"] == "https://simbad.u-strasbg.fr/simbad/sim-basic?Ident=IC0001"
    assert ic1["ALADIN"] == "https://aladin.cds.unistra.fr/AladinLite/?target=IC0001"
    assert ic1["Astrobin"] == "https://www.astrobin.com/search/?q=IC0001"


def test_catalogs_do_not_expose_technical_columns():
    c = Catalogs()
    for catalog in [c.NGC, c.MESSIER, c.BRIGHT_STARS]:
        for col in TECHNICAL_COLUMNS:
            assert col not in catalog.columns


def test_raw_catalogs_keep_technical_columns():
    from apts.catalogs.ngc import get_ngc, get_ngc_raw
    from apts.catalogs.messier import get_messier, get_messier_raw
    from apts.catalogs.stars import get_bright_stars, get_bright_stars_raw

    for clean, raw in [
        (get_ngc(), get_ngc_raw()),
        (get_messier(), get_messier_raw()),
        (get_bright_stars(), get_bright_stars_raw()),
    ]:
        for col in TECHNICAL_COLUMNS:
            assert col not in clean.columns
        for col in ("ra_hours", "dec_degrees", "Magnitude_float",
                    "sin_dec", "cos_dec_cos_ra", "cos_dec_sin_ra"):
            assert col in raw.columns

    # NGC additionally pre-computes normalized identifiers; Messier/Stars
    # additionally pre-compute Skyfield objects.
    assert all(
        col in get_ngc_raw().columns for col in ("NGC_norm", "IC_norm", "Name_norm")
    )
    assert "skyfield_object" in get_messier_raw().columns
    assert "skyfield_object" in get_bright_stars_raw().columns

