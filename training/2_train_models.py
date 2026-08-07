import pandas as pd
import joblib

from sklearn.model_selection import train_test_split

from sklearn.preprocessing import LabelEncoder

from sklearn.metrics import accuracy_score

from sklearn.tree import DecisionTreeClassifier

from sklearn.ensemble import RandomForestClassifier

from sklearn.linear_model import LogisticRegression

from sklearn.neighbors import KNeighborsClassifier

from sklearn.svm import SVC

# -----------------------------
# LOAD DATASET
# -----------------------------

df = pd.read_csv("data/fertilizer_recommendation_2000.csv")

# -----------------------------
# ENCODING
# -----------------------------

crop_encoder = LabelEncoder()
soil_encoder = LabelEncoder()
fert_encoder = LabelEncoder()

df["Crop"] = crop_encoder.fit_transform(df["Crop"])
df["Soil_Type"] = soil_encoder.fit_transform(df["Soil_Type"])
df["Fertilizer"] = fert_encoder.fit_transform(df["Fertilizer"])

# Save encoders

joblib.dump(crop_encoder, "models/crop_encoder.pkl")
joblib.dump(soil_encoder, "models/soil_encoder.pkl")
joblib.dump(fert_encoder, "models/fert_encoder.pkl")

# -----------------------------
# FEATURES
# -----------------------------

X = df.drop("Fertilizer", axis=1)
y = df["Fertilizer"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

# -----------------------------
# MODELS
# -----------------------------

models = {

    "Decision Tree":
        DecisionTreeClassifier(random_state=42),

    "Random Forest":
        RandomForestClassifier(
            n_estimators=200,
            random_state=42
        ),

    "Logistic Regression":
        LogisticRegression(max_iter=1000),

    "KNN":
        KNeighborsClassifier(),

    "SVM":
        SVC()

}

# -----------------------------
# TRAIN
# -----------------------------

results = {}

best_accuracy = 0
best_model = None
best_name = ""

print("\nTraining Started...\n")

for name, model in models.items():

    model.fit(X_train, y_train)

    pred = model.predict(X_test)

    acc = accuracy_score(y_test, pred)

    results[name] = acc

    print(f"{name} Accuracy : {acc:.4f}")

    if acc > best_accuracy:

        best_accuracy = acc

        best_model = model

        best_name = name

# -----------------------------
# SAVE BEST MODEL
# -----------------------------

joblib.dump(
    best_model,
    "models/best_random_forest.pkl"
)

print("\n--------------------------------")

print("Best Model :", best_name)

print("Accuracy :", best_accuracy)

print("--------------------------------")

print("\nModel Saved Successfully")