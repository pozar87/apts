from apts.catalogs import Catalogs

def test_messier_catalog():
  c = Catalogs.MESSIER
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
  largest_objects = c.sort_values(by='Width', key=lambda x: x.apply(lambda y: y.magnitude if hasattr(y, 'magnitude') else y), ascending=False)
  assert largest_objects.iloc[0]["Name"] == "Andromeda Galaxy"
  assert largest_objects.iloc[0]["Messier"] == "M31"
  assert largest_objects.iloc[0]["NGC"] == "NGC 224"
  # Check data types
  assert c["Messier"].dtype == "object"
  assert c["NGC"].dtype == "object"
  assert c["Name"].dtype == "object"
  assert c["Type"].dtype == "object"
  # Now using pint units, so dtype is object
  assert hasattr(c["RA"].iloc[0], 'magnitude')
  assert hasattr(c["Dec"].iloc[0], 'magnitude')
  assert hasattr(c["Distance"].iloc[0], 'magnitude')
  assert hasattr(c["Width"].iloc[0], 'magnitude')
