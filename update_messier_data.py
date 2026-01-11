from typing import Any, cast

import pandas as pd


def update_messier_data():
    """
    Updates the messier.csv file with PosAng values from the ngc.csv file.
    """
    try:
        messier_df = pd.read_csv("apts/data/messier.csv")
        ngc_df = pd.read_csv("apts/data/ngc.csv", sep=";")

        # Create a mapping from NGC name to PosAng
        ngc_name_to_posang = ngc_df.set_index("Name")["PosAng"].to_dict()

        # Update the PosAng in messier_df
        # The 'Name' in messier.csv often corresponds to an NGC name.
        messier_df["PosAng"] = messier_df["Name"].map(cast(Any, ngc_name_to_posang))

        # Fill any NaNs that might result from no match with 0.0
        # and ensure the column is of type float
        messier_df["PosAng"] = messier_df["PosAng"].fillna(0.0).astype(float)

        messier_df.to_csv("apts/data/messier.csv", index=False)
        print("Successfully updated apts/data/messier.csv with PosAng values.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    update_messier_data()
