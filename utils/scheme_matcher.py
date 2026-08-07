import pandas as pd
from pathlib import Path

# ==========================================================
# Load Government Schemes
# ==========================================================

SCHEME_FILE = (
    Path(__file__).parent.parent
    / "knowledge"
    / "government_schemes.csv"
)

schemes = pd.read_csv(SCHEME_FILE)

# ==========================================================
# Clean Data
# ==========================================================

text_columns = [
    "State",
    "District",
    "Crop",
    "Need",
    "Gender",
    "Keywords"
]

for col in text_columns:
    if col in schemes.columns:
        schemes[col] = (
            schemes[col]
            .fillna("")
            .astype(str)
            .str.strip()
        )

# ==========================================================
# Scheme Matcher
# ==========================================================

def match_schemes(
    state=None,
    district=None,
    crop=None,
    land_area=None,
    gender=None,
    age=None,
    organic=False,
    irrigation=False,
    fpo=False,
    need=None
):

    df = schemes.copy()

    # Initialize Score
    df["Score"] = 0

    # -------------------------------------------------
    # State
    # -------------------------------------------------

    if state:

        mask = (
            (df["State"].str.lower() == state.lower())
            |
            (df["State"].str.lower() == "all")
        )

        df = df[mask]

        df.loc[
            df["State"].str.lower() == state.lower(),
            "Score"
        ] += 25

    # -------------------------------------------------
    # District
    # -------------------------------------------------

    if district:

        mask = (
            (df["District"].str.lower() == district.lower())
            |
            (df["District"].str.lower() == "all")
        )

        df = df[mask]

        df.loc[
            df["District"].str.lower() == district.lower(),
            "Score"
        ] += 10

    # -------------------------------------------------
    # Crop
    # -------------------------------------------------

    if crop:

        mask = (
            (df["Crop"].str.lower() == crop.lower())
            |
            (df["Crop"].str.lower() == "all")
        )

        df = df[mask]

        df.loc[
            df["Crop"].str.lower() == crop.lower(),
            "Score"
        ] += 25

    # -------------------------------------------------
    # Land Area
    # -------------------------------------------------

    if land_area is not None:

        df = df[
            (df["Min_Land_Acres"] <= land_area)
            &
            (df["Max_Land_Acres"] >= land_area)
        ]

        df["Score"] += 10

    # -------------------------------------------------
    # Gender
    # -------------------------------------------------

    if gender:

        mask = (
            (df["Gender"].str.lower() == gender.lower())
            |
            (df["Gender"].str.lower() == "all")
        )

        df = df[mask]

    # -------------------------------------------------
    # Age
    # -------------------------------------------------

    if age is not None:

        df = df[
            (df["Age_Min"] <= age)
            &
            (df["Age_Max"] >= age)
        ]

    # -------------------------------------------------
    # Need (Search Need + Keywords)
    # -------------------------------------------------

    if need:

        need = need.lower()

        mask = (
            df["Need"]
            .str.lower()
            .str.contains(need, na=False)
        ) | (
            df["Keywords"]
            .str.lower()
            .str.contains(need, na=False)
        )

        df = df[mask]

        df["Score"] += 40

    # -------------------------------------------------
    # Organic
    # -------------------------------------------------

    if organic:
        df["Score"] += 5

    # -------------------------------------------------
    # Irrigation
    # -------------------------------------------------

    if irrigation:
        df["Score"] += 5

    # -------------------------------------------------
    # FPO
    # -------------------------------------------------

    if fpo:
        df["Score"] += 5

    # -------------------------------------------------
    # Sort
    # -------------------------------------------------

    df = df.sort_values(
        by="Score",
        ascending=False
    )

    return df.to_dict(orient="records")