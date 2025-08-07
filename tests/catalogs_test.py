from apts.catalogs import Catalogs


def test_messier_catalog():
    c = Catalogs().MESSIER
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
    # Sort using magnitude value of Width
    largest_objects = c.sort_values(
        by="Width",
        key=lambda x: x.apply(lambda y: y.magnitude if hasattr(y, "magnitude") else y),
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

    assert hasattr(c["Width"].iloc[0], "magnitude")
    assert hasattr(c["Width"].iloc[0], "units")
    assert c["Width"].iloc[0].units == "arcminute"

    assert hasattr(c["Magnitude"].iloc[0], "magnitude")
    assert hasattr(c["Magnitude"].iloc[0], "units")
    assert c["Magnitude"].iloc[0].units == "mag"
