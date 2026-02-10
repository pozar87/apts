import re
from typing import Any, cast

import pandas as pd


def update_messier_data():
    """
    Updates the messier.csv file with PosAng values from the ngc.csv file.
    """
    try:
        messier_df = pd.read_csv("apts/data/messier.csv")
        ngc_df = pd.read_csv("apts/data/ngc.csv", sep=";")

        # Create a mapping from Messier number to PosAng
        messier_to_posang = {}
        for _, row in ngc_df.iterrows():
            identifiers = str(row["Identifiers"])
            messier_match = re.search(r"M\s*(\d+)", identifiers)
            if messier_match:
                messier_num = f"M{messier_match.group(1)}"
                messier_to_posang[messier_num] = row["PosAng"]

        # Update the PosAng in messier_df
        messier_df["PosAng"] = messier_df["Messier"].map(cast(Any, messier_to_posang))

        # Fill any NaNs that might result from no match with 0.0
        # and ensure the column is of type float
        messier_df["PosAng"] = messier_df["PosAng"].fillna(0.0).astype(float)

        messier_df.to_csv("apts/data/messier.csv", index=False)
        print("Successfully updated apts/data/messier.csv with PosAng values.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    update_messier_data()
