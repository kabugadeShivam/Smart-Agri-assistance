import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# -----------------------------
# Load Dataset
# -----------------------------

df = pd.read_csv("data/fertilizer_recommendation_2000.csv")

print("Dataset Loaded Successfully")
print(df.head())

# -----------------------------
# Label Encoding
# -----------------------------

crop_encoder = LabelEncoder()
soil_encoder = LabelEncoder()
fert_encoder = LabelEncoder()

df["Crop"] = crop_encoder.fit_transform(df["Crop"])
df["Soil_Type"] = soil_encoder.fit_transform(df["Soil_Type"])
df["Fertilizer"] = fert_encoder.fit_transform(df["Fertilizer"])

# -----------------------------
# Features and Target
# -----------------------------

X = df.drop("Fertilizer", axis=1)
y = df["Fertilizer"]

# -----------------------------
# Train Test Split
# -----------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

print("\nTraining Samples :", len(X_train))
print("Testing Samples :", len(X_test))

# -----------------------------
# Save Encoders
# -----------------------------

joblib.dump(crop_encoder, "models/crop_encoder.pkl")
joblib.dump(soil_encoder, "models/soil_encoder.pkl")
joblib.dump(fert_encoder, "models/fert_encoder.pkl")

print("\nEncoders Saved Successfully")