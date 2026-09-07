# 🌾 Smart Agriculture AI

An AI-powered **Smart Agriculture Assistant** built with Python and Streamlit to support farmers with crop, fertilizer, disease, yield, weather and government-scheme assistance.

## 🚀 Live Demo

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://smart-agri-assistance.streamlit.app)

👉 **[Open Smart Agriculture AI](https://smart-agri-assistance.streamlit.app)**

## ✨ Main Features

- 👨‍🌾 Farmer registration and profile management
- 🌾 Fertilizer recommendation using a trained ML model
- 🌿 AI plant disease detection from leaf images
- 📈 Crop yield prediction
- 🌦️ Weather-assisted recommendations
- 🤖 AI advisor and chatbot
- 🏛️ Government scheme matching
- 📊 Prediction history and dashboard

## 🛠️ Tech Stack

- **Python**
- **Streamlit**
- **Pandas / NumPy**
- **Scikit-learn**
- **TensorFlow / Keras**
- **SQLite**
- **Joblib**

## 📁 Project Structure

```text
Smart-Agri-assistance/
│
├── app.py                         # Streamlit entry point
├── pages/                         # Streamlit application pages
│   ├── 00_Login.py
│   ├── 1_Home.py
│   ├── 2_Prediction.py
│   ├── 4_Model_Analysis.py
│   ├── 5_History.py
│   ├── 6_About.py
│   ├── 8_Disease_Detection.py
│   ├── 9_Yield_Prediction.py
│   ├── 10_AI_Advisor.py
│   ├── 11_AI_Chatbot.py
│   └── 12_Government_Scheme_Matcher.py
│
├── utils/                        # Shared application logic
│   ├── auth.py
│   ├── database.py
│   ├── disease_predict.py
│   ├── disease_info.py
│   ├── yield_predict.py
│   ├── farmer_memory.py
│   └── ...
│
├── models/                       # Trained ML/DL models
│   ├── best_random_forest.pkl
│   ├── plant_disease_model.keras
│   └── yield_prediction_model.pkl
│
├── database/                     # Database initialization code
│   └── init_db.py
│
├── agriculture_knowledge.csv     # Agriculture knowledge base
├── requirements.txt              # Python dependencies
├── .gitignore                    # Local/cache/secrets exclusions
└── README.md
```

> Training-only datasets, local databases, cache files, duplicate pages and temporary test scripts are intentionally excluded from the repository.

## ▶️ Run Locally

```bash
git clone https://github.com/kabugadeShivam/Smart-Agri-assistance.git
cd Smart-Agri-assistance
pip install -r requirements.txt
streamlit run app.py
```

## 🎯 Objective

The project aims to make practical agricultural intelligence accessible through a simple web application, combining machine learning, computer vision, farmer profiles and AI-assisted recommendations.

## 👨‍💻 Developer

**Shivam Kabugade**

GitHub: https://github.com/kabugadeShivam
