import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import joblib
import os

st.set_page_config(
    page_title="Model Analysis",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Model Analysis")

model_path = "models/best_random_forest.pkl"

if not os.path.exists(model_path):
    st.error("Model not found.")
    st.stop()

model = joblib.load(model_path)

st.success("✅ Random Forest Model Loaded Successfully")

if hasattr(model, "feature_importances_"):

    features = [
        "Crop",
        "N",
        "P",
        "K",
        "Temperature",
        "Humidity",
        "Moisture",
        "Soil_Type"
    ]

    importance = pd.DataFrame({
        "Feature": features,
        "Importance": model.feature_importances_
    })

    importance = importance.sort_values(
        by="Importance",
        ascending=True
    )

    fig, ax = plt.subplots(figsize=(8,5))

    ax.barh(
        importance["Feature"],
        importance["Importance"]
    )

    st.pyplot(fig)

else:

    st.info("Feature importance not available.")