import streamlit as st
import pandas as pd
import joblib

from utils.weather import get_weather

# -----------------------------
# Load Model
# -----------------------------

model = joblib.load("models/crop_compatibility_model.pkl")

crop_encoder = joblib.load("models/crop_type_encoder.pkl")

soil_encoder = joblib.load("models/soil_type_encoder.pkl")

irrigation_encoder = joblib.load("models/irrigation_encoder.pkl")

# -----------------------------
# Page Title
# -----------------------------

st.title("🌾 Crop Compatibility Checker")

st.write(
    "Check whether a crop is suitable for your soil and climate."
)

st.divider()

# -----------------------------
# Inputs
# -----------------------------

crop = st.selectbox(
    "Crop",
    crop_encoder.classes_
)

soil = st.selectbox(
    "Soil Type",
    soil_encoder.classes_
)

city = st.text_input(
    "City",
    placeholder="Enter City"
)

farm_size = st.number_input(
    "Farm Size (Acres)",
    min_value=0.5,
    max_value=100.0,
    value=2.0
)

irrigation = st.selectbox(
    "Irrigation Available",
    irrigation_encoder.classes_
)

soil_ph = st.slider(
    "Soil pH",
    4.0,
    9.0,
    6.5
)

soil_n = st.slider(
    "Soil Nitrogen",
    0,
    150,
    50
)

organic = st.slider(
    "Organic Matter (%)",
    0.0,
    10.0,
    2.0
)

temperature = 25
humidity = 60
rainfall = 100

# -----------------------------
# Weather API
# -----------------------------

if city:

    weather = get_weather(city)

    if weather:

        temperature = weather["temperature"]

        humidity = weather["humidity"]

        st.success(f"Weather Loaded for {city}")

        st.metric(
            "Temperature",
            f"{temperature} °C"
        )

        st.metric(
            "Humidity",
            f"{humidity}%"
        )

        rainfall = st.slider(
            "Rainfall (mm)",
            0,
            500,
            100
        )

    else:

        st.error("Unable to fetch weather.")

st.divider()

# -----------------------------
# Prediction
# -----------------------------

if st.button("Check Compatibility"):

    sample = pd.DataFrame({

        "Crop_Type":[crop_encoder.transform([crop])[0]],

        "Soil_Type":[soil_encoder.transform([soil])[0]],

        "Farm_Size_Acres":[farm_size],

        "Irrigation_Available":[irrigation_encoder.transform([irrigation])[0]],

        "Soil_pH":[soil_ph],

        "Soil_Nitrogen":[soil_n],

        "Soil_Organic_Matter":[organic],

        "Temperature":[temperature],

        "Rainfall":[rainfall],

        "Humidity":[humidity]

    })

    prediction = model.predict(sample)[0]

    if prediction == 1:

        st.success("✅ Compatible")

        st.balloons()

    else:

        st.error("❌ Not Compatible")