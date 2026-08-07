import streamlit as st
import pandas as pd
import joblib

from utils.database import insert_prediction
from utils.weather import get_weather
from utils.session_manager import save_prediction

# ----------------------------
# Load Model
# ----------------------------

model = joblib.load("models/best_random_forest.pkl")
crop_encoder = joblib.load("models/crop_encoder.pkl")
soil_encoder = joblib.load("models/soil_encoder.pkl")
fert_encoder = joblib.load("models/fert_encoder.pkl")

# ----------------------------
# Page Title
# ----------------------------

st.title("🌱 Fertilizer Recommendation System")

st.write("Enter the crop and soil details below.")

st.divider()

# ----------------------------
# User Inputs
# ----------------------------

crop = st.selectbox(
    "🌾 Crop",
    crop_encoder.classes_
)

soil = st.selectbox(
    "🪨 Soil Type",
    soil_encoder.classes_
)

city = st.text_input(
    "📍 City",
    placeholder="Enter your city (e.g. Pune)"
)

# Default values
temperature = 25
humidity = 60

# ----------------------------
# Weather API
# ----------------------------

if city:

    weather = get_weather(city)

    if weather:

        temperature = weather["temperature"]
        humidity = weather["humidity"]

        st.success(f"✅ Live Weather Loaded for {city}")

        st.markdown("## 🌦 Current Weather")

        col1, col2 = st.columns(2)

        col1.metric(
            "🌡 Temperature",
            f"{temperature} °C"
        )

        col2.metric(
            "💧 Humidity",
            f"{humidity}%"
        )

        col3, col4 = st.columns(2)

        col3.metric(
            "🌬 Wind Speed",
            f"{weather['wind']} m/s"
        )

        col4.metric(
            "🧭 Pressure",
            f"{weather['pressure']} hPa"
        )

        st.info(
            f"☁ Weather Condition : {weather['weather']}"
        )

    else:
        st.error("❌ Unable to fetch weather. Please check the city name.")

st.divider()

# ----------------------------
# Soil Parameters
# ----------------------------

N = st.slider(
    "Nitrogen (N)",
    0,
    150,
    50
)

P = st.slider(
    "Phosphorus (P)",
    0,
    100,
    30
)

K = st.slider(
    "Potassium (K)",
    0,
    100,
    30
)

moisture = st.slider(
    "Soil Moisture (%)",
    0,
    100,
    50
)

st.divider()

# ----------------------------
# Predict Button
# ----------------------------

if st.button("🌾 Recommend Fertilizer"):

    crop_value = crop_encoder.transform([crop])[0]
    soil_value = soil_encoder.transform([soil])[0]

    sample = pd.DataFrame({
        "Crop": [crop_value],
        "N": [N],
        "P": [P],
        "K": [K],
        "Temperature": [temperature],
        "Humidity": [humidity],
        "Moisture": [moisture],
        "Soil_Type": [soil_value]
    })

    prediction = model.predict(sample)

    fertilizer = fert_encoder.inverse_transform(prediction)
    save_prediction(
    "fertilizer",
    fertilizer[0]
)

    # Save Prediction to Database
    insert_prediction(
        crop,
        soil,
        N,
        P,
        K,
        temperature,
        humidity,
        moisture,
        fertilizer[0]
    )

    st.success(
        f"✅ Recommended Fertilizer: **{fertilizer[0]}**"
    )

    st.balloons()