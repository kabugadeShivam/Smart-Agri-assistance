import streamlit as st

from utils.auth import (
    is_logged_in,
    current_farmer,
    current_profile
)

from utils.database import get_connection

# =====================================================
# Page Config
# =====================================================

st.set_page_config(
    page_title="Smart Agri Dashboard",
    page_icon="🌾",
    layout="wide"
)

# =====================================================
# Login Check
# =====================================================

if not is_logged_in():

    st.warning("Please login first.")

    st.stop()

# =====================================================
# Farmer Profile
# =====================================================

profile = current_profile()

st.title("🌾 Smart Agri AI Dashboard")

st.write(
    f"Welcome **{profile['farmer_name']}** 👋"
)

st.divider()

# =====================================================
# Farmer Information
# =====================================================

st.subheader("👨‍🌾 Farmer Profile")

c1, c2, c3, c4 = st.columns(4)

c1.metric("🌾 Crop", profile["crop"] or "Not Updated")
c2.metric("🌱 Land", f"{profile['land_area']} Acres")
c3.metric("🪨 Soil", profile["soil_type"] or "Not Updated")
c4.metric("💧 Irrigation", profile["irrigation"] or "Not Updated")

c5, c6, c7, c8 = st.columns(4)

c5.metric("📍 State", profile["state"] or "-")
c6.metric("🏘 District", profile["district"] or "-")
c7.metric("🏡 Village", profile["village"] or "-")
c8.metric("🤝 FPO", profile["fpo_member"] or "No")

st.divider()

# =====================================================
# AI Modules
# =====================================================

st.subheader("🤖 Smart Agriculture Modules")

a, b, c = st.columns(3)

with a:

    st.info("🦠 Disease Detection")

    st.write(
        "Upload crop leaf images for disease detection."
    )

with b:

    st.info("🌾 Yield Prediction")

    st.write(
        "Predict expected production and revenue."
    )

with c:

    st.info("🏛 Government Schemes")

    st.write(
        "AI automatically matches eligible schemes."
    )

d, e, f = st.columns(3)

with d:

    st.info("📈 Market Intelligence")

    st.write(
        "Find best mandi prices."
    )

with e:

    st.info("🌤 Weather")

    st.write(
        "Weather forecast and farming alerts."
    )

with f:

    st.info("🤖 AI Advisor")

    st.write(
        "Personalized farming recommendations."
    )

st.divider()

# =====================================================
# Recent Predictions
# =====================================================

st.subheader("📊 Recent Prediction History")

conn = get_connection()

cursor = conn.cursor()

cursor.execute(
    """
    SELECT *

    FROM prediction_history

    WHERE farmer_id=?

    ORDER BY created_at DESC

    LIMIT 10
    """,
    (current_farmer(),)
)

rows = cursor.fetchall()

conn.close()

if len(rows) == 0:

    st.info("No prediction history available.")

else:

    for row in rows:

        with st.expander(
            f"{row['prediction_type']} • {row['created_at']}"
        ):

            st.write(
                f"**Prediction:** {row['prediction']}"
            )

            st.write(
                f"**Confidence:** {row['confidence']}"
            )

st.divider()

# =====================================================
# Quick Actions
# =====================================================

st.subheader("⚡ Quick Actions")

q1, q2, q3, q4 = st.columns(4)

with q1:

    if st.button("🦠 Disease Detection", use_container_width=True):
        st.switch_page("pages/8_Disease_Detection.py")

with q2:

    if st.button("🌾 Yield Prediction", use_container_width=True):
        st.switch_page("pages/9_Yield_Prediction.py")

with q3:

    if st.button("🏛 Government Schemes", use_container_width=True):
        st.switch_page("pages/12_Government_Scheme_Matcher.py")

with q4:

    if st.button("🤖 AI Advisor", use_container_width=True):
        st.switch_page("pages/11_AI_Chatbot.py")