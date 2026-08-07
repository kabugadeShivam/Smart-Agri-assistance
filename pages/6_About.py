import streamlit as st

# --------------------------------------
# PAGE CONFIG
# --------------------------------------

st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
    layout="wide"
)

# --------------------------------------
# TITLE
# --------------------------------------

st.title("ℹ️ About Smart Agriculture AI")

st.markdown("---")

# --------------------------------------
# PROJECT
# --------------------------------------

st.header("🌾 Project Overview")

st.write("""
Smart Agriculture AI is a Machine Learning based web application
that recommends the most suitable fertilizer for crops based on:

- Crop Type
- Soil Type
- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)
- Temperature
- Humidity
- Moisture

The application helps farmers make informed fertilizer decisions
using trained Machine Learning models.
""")

st.markdown("---")

# --------------------------------------
# TECHNOLOGIES
# --------------------------------------

st.header("🛠 Technologies Used")

tech1, tech2 = st.columns(2)

with tech1:
    st.success("🐍 Python")
    st.success("📊 Pandas")
    st.success("🔢 NumPy")
    st.success("🤖 Scikit-Learn")

with tech2:
    st.success("🌐 Streamlit")
    st.success("📈 Matplotlib")
    st.success("💾 Joblib")
    st.success("🗄 SQLite (Upcoming)")

st.markdown("---")

# --------------------------------------
# MACHINE LEARNING MODELS
# --------------------------------------

st.header("🤖 Machine Learning Models")

st.table({
    "Model": [
        "Decision Tree",
        "Random Forest",
        "Logistic Regression",
        "K-Nearest Neighbors",
        "Support Vector Machine",
        "XGBoost"
    ],
    "Status": [
        "✅ Trained",
        "✅ Trained",
        "✅ Trained",
        "✅ Trained",
        "✅ Trained",
        "✅ Trained"
    ]
})

st.markdown("---")

# --------------------------------------
# PROJECT FEATURES
# --------------------------------------

st.header("🚀 Features")

st.checkbox("Fertilizer Recommendation", value=True)
st.checkbox("Interactive Dashboard", value=True)
st.checkbox("Model Comparison", value=True)
st.checkbox("Prediction History", value=True)
st.checkbox("CSV Download", value=True)
st.checkbox("Feature Importance", value=True)

st.markdown("---")

# --------------------------------------
# FUTURE ENHANCEMENTS
# --------------------------------------

st.header("🔮 Future Enhancements")

st.write("""
- 🌦 Live Weather API Integration
- 🌱 Crop Recommendation
- 🍃 Plant Disease Detection
- 📈 Crop Yield Prediction
- 💰 Market Price Prediction
- 🛰 Satellite Image Analysis
- 📱 Mobile Application
- ☁ Cloud Deployment
""")

st.markdown("---")

# --------------------------------------
# DEVELOPER
# --------------------------------------

st.header("👨‍💻 Developer")

st.info("""
Machine Learning Portfolio Project

Built using Python, Scikit-Learn and Streamlit.

This project demonstrates:

✔ Data Preprocessing

✔ Machine Learning

✔ Model Evaluation

✔ Hyperparameter Tuning

✔ Streamlit Deployment
""")

st.markdown("---")

# --------------------------------------
# VERSION
# --------------------------------------

st.header("📌 Version")

st.write("""
Version : **1.0**

Status : **Production Ready**

Year : **2026**
""")

st.markdown("---")

# --------------------------------------
# FOOTER
# --------------------------------------

st.caption("🌾 Smart Agriculture AI | Version 1.0")