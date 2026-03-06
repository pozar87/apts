
import time
import pandas as pd
import numpy as np
from apts.units import get_unit_registry

def test_pint_speed():
    size = 14000
    values = np.random.randn(size)
    ureg = get_unit_registry()

    start = time.time()
    q = values * ureg.mag
    print(f"Single Quantity creation took: {time.time() - start:.4f}s")

    start = time.time()
    l = list(values * ureg.mag)
    print(f"List of Quantities creation took: {time.time() - start:.4f}s")

    df = pd.DataFrame({'val': values})

    start = time.time()
    df['Magnitude'] = l
    print(f"Assigning list to DF took: {time.time() - start:.4f}s")

    df2 = pd.DataFrame({'val': values})
    start = time.time()
    # This might not work as expected in Pandas without pint-pandas
    df2['Magnitude'] = q
    print(f"Assigning single Quantity to DF took: {time.time() - start:.4f}s")
    print(f"DF2 Magnitude type: {type(df2['Magnitude'].iloc[0])}")

if __name__ == "__main__":
    test_pint_speed()
