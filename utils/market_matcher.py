import pandas as pd
from pathlib import Path

# ==========================================================
# Load Market Dataset
# ==========================================================

MARKET_FILE = (
    Path(__file__).parent.parent
    / "knowledge"
    / "market_prices.csv"
)

market_df = pd.read_csv(MARKET_FILE)


# ==========================================================
# Market Matcher
# ==========================================================

def match_market(
    crop,
    state=None,
    district=None
):

    df = market_df.copy()

    # -----------------------------------
    # Crop Filter
    # -----------------------------------

    df = df[
        df["Crop"].str.lower() == crop.lower()
    ]

    # -----------------------------------
    # State Filter
    # -----------------------------------

    if state:

        df = df[
            df["State"].str.lower() == state.lower()
        ]

    # -----------------------------------
    # District Filter
    # -----------------------------------

    if district:

        district_df = df[
            df["District"].str.lower() == district.lower()
        ]

        if len(district_df) > 0:
            df = district_df

    if len(df) == 0:
        return []

    # -----------------------------------
    # Highest Price First
    # -----------------------------------

    df = df.sort_values(
        by="Modal_Price",
        ascending=False
    )

    return df.head(5).to_dict("records")