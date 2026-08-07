import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

print("Loading Dataset...")

df = pd.read_csv("data/Soil-Climate-data.csv")

# --------------------------
# Remove missing values
# --------------------------

df = df.dropna()

# --------------------------
# Label Encoders
# --------------------------

crop_encoder = LabelEncoder()
soil_encoder = LabelEncoder()
irrigation_encoder = LabelEncoder()

df["Crop_Type"] = crop_encoder.fit_transform(df["Crop_Type"])
df["Soil_Type"] = soil_encoder.fit_transform(df["Soil_Type"])
df["Irrigation_Available"] = irrigation_encoder.fit_transform(df["Irrigation_Available"])

# --------------------------
# Features and Target
# --------------------------

X = df.drop("Compatible", axis=1)
y = df["Compatible"]

# --------------------------
# Train Test Split
# --------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# --------------------------
# Decision Tree
# --------------------------

dt = DecisionTreeClassifier(random_state=42)
dt.fit(X_train, y_train)

dt_pred = dt.predict(X_test)

dt_acc = accuracy_score(y_test, dt_pred)

print(f"Decision Tree Accuracy : {dt_acc:.4f}")

# --------------------------
# Random Forest
# --------------------------

rf = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

rf.fit(X_train, y_train)

rf_pred = rf.predict(X_test)

rf_acc = accuracy_score(y_test, rf_pred)

print(f"Random Forest Accuracy : {rf_acc:.4f}")

# --------------------------
# Best Model
# --------------------------

if rf_acc >= dt_acc:

    best_model = rf
    best_name = "Random Forest"
    best_acc = rf_acc

else:

    best_model = dt
    best_name = "Decision Tree"
    best_acc = dt_acc

print("\n----------------------------")
print("Best Model :", best_name)
print("Accuracy :", round(best_acc,4))
print("----------------------------")

# --------------------------
# Save Model
# --------------------------

joblib.dump(
    best_model,
    "models/crop_compatibility_model.pkl"
)

joblib.dump(
    crop_encoder,
    "models/crop_type_encoder.pkl"
)

joblib.dump(
    soil_encoder,
    "models/soil_type_encoder.pkl"
)

joblib.dump(
    irrigation_encoder,
    "models/irrigation_encoder.pkl"
)

print("\nModel Saved Successfully!")