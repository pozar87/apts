import pytest
from default import *

def test_messier_catalog():
  c = Catalogs.MESSIER
  # Messier catalog contains 110 objects
  assert len(c) == 110
  # M13 is  Hercules Globular Cluster - NGC 6205 (index starts from 0)
  assert c.iloc[12]["NGC"] == "NGC 6205"
  # M45 is Pleiades (index starts from 0)
  assert c.iloc[44]["Messier"] == "M45"
  # M82 is Cigar Galaxy - NGC 3034 (index starts from 0)
  assert c.iloc[81]["NGC"] == "NGC 3034"
