import streamlit as st
import sqlite3
import pandas as pd
from pathlib import Path

# -----------------------------
# PAGE CONFIG
# -----------------------------

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Smart Agriculture Dashboard")

st.divider()

# -----------------------------
# DATABASE
# -----------------------------

DATABASE = Path(__file__).parent.parent / "database" / "predictions.db"

conn = sqlite3.connect(DATABASE)

df = pd.read_sql_query(
    "SELECT * FROM predictions",
    conn
)

conn.close()

# -----------------------------
# CHECK DATA
# -----------------------------

if df.empty:

    st.warning("No predictions found.")

    st.stop()

# -----------------------------
# METRICS
# -----------------------------

total_predictions = len(df)

most_crop = df["crop"].mode()[0]

most_fertilizer = df["fertilizer"].mode()[0]

unique_crops = df["crop"].nunique()

c1, c2, c3, c4 = st.columns(4)

c1.metric("Total Predictions", total_predictions)

c2.metric("Most Predicted Crop", most_crop)

c3.metric("Top Fertilizer", most_fertilizer)

c4.metric("Unique Crops", unique_crops)

st.divider()

# -----------------------------
# RECENT PREDICTIONS
# -----------------------------

st.subheader("📝 Recent Predictions")

st.dataframe(
    df.sort_values(
        "prediction_time",
        ascending=False
    ),
    use_container_width=True
)

st.divider()

# -----------------------------
# CROP COUNT
# -----------------------------

st.subheader("🌾 Crop Distribution")

crop_count = df["crop"].value_counts()

st.bar_chart(crop_count)

st.divider()

# -----------------------------
# FERTILIZER COUNT
# -----------------------------

st.subheader("🧪 Fertilizer Distribution")

fert_count = df["fertilizer"].value_counts()

st.bar_chart(fert_count)