import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# -----------------------------
# Load Dataset
# -----------------------------

df = pd.read_csv("data/crop_yield_dataset_500.csv")

print(df.head())

# -----------------------------
# Features
# -----------------------------

X = df[[
    "Crop",
    "State",
    "Soil_Type",
    "Rainfall_mm",
    "Temperature_C",
    "Area_Hectare"
]]

# Target

y = df["Yield_ton_per_hectare"]

# -----------------------------
# Categorical Columns
# -----------------------------

categorical = [
    "Crop",
    "State",
    "Soil_Type"
]

numeric = [
    "Rainfall_mm",
    "Temperature_C",
    "Area_Hectare"
]

preprocessor = ColumnTransformer(

    transformers=[

        (
            "cat",
            OneHotEncoder(handle_unknown="ignore"),
            categorical
        ),

        (
            "num",
            "passthrough",
            numeric
        )

    ]

)

# -----------------------------
# Model
# -----------------------------

model = Pipeline([

    ("preprocessor", preprocessor),

    (
        "regressor",
        RandomForestRegressor(
            n_estimators=200,
            random_state=42
        )
    )

])

# -----------------------------
# Train/Test Split
# -----------------------------

X_train, X_test, y_train, y_test = train_test_split(

    X,
    y,
    test_size=0.2,
    random_state=42

)

# -----------------------------
# Train
# -----------------------------

model.fit(
    X_train,
    y_train
)

# -----------------------------
# Prediction
# -----------------------------

prediction = model.predict(X_test)

mae = mean_absolute_error(
    y_test,
    prediction
)

r2 = r2_score(
    y_test,
    prediction
)

print("\nModel Performance")

print("MAE :", mae)

print("R2 Score :", r2)

# -----------------------------
# Save
# -----------------------------

joblib.dump(

    model,

    "models/yield_prediction_model.pkl"

)

print("\nYield Model Saved Successfully!")