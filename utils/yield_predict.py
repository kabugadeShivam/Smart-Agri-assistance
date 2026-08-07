import joblib
import pandas as pd

# Load model once
model = joblib.load("models/yield_prediction_model.pkl")


def predict_yield(
    crop,
    state,
    soil,
    rainfall,
    temperature,
    area
):

    sample = pd.DataFrame({

        "Crop": [crop],

        "State": [state],

        "Soil_Type": [soil],

        "Rainfall_mm": [rainfall],

        "Temperature_C": [temperature],

        "Area_Hectare": [area]

    })

    predicted_yield = model.predict(sample)[0]

    production = predicted_yield * area

    return predicted_yield, production