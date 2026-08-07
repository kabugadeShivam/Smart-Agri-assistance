import streamlit as st
import sqlite3
import pandas as pd
from pathlib import Path

st.set_page_config(
    page_title="Prediction History",
    page_icon="📜",
    layout="wide"
)

st.title("📜 Prediction History")

DATABASE = Path(__file__).parent.parent / "database" / "predictions.db"

conn = sqlite3.connect(DATABASE)

df = pd.read_sql_query(
    "SELECT * FROM predictions ORDER BY prediction_time DESC",
    conn
)

conn.close()

if df.empty:
    st.warning("No prediction history found.")
    st.stop()

st.subheader("🔍 Search")

crop = st.text_input("Search Crop")

if crop != "":
    df = df[df["crop"].str.contains(crop, case=False)]

st.dataframe(df, use_container_width=True)

csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    "📥 Download CSV",
    csv,
    "prediction_history.csv",
    "text/csv"
)