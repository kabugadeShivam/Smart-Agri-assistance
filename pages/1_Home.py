import streamlit as st

from utils.auth import is_logged_in
from utils.auth import current_farmer
from utils.profile_manager import get_profile

from utils.ai_engine.context_builder import build_context
from utils.ai_engine.recommendation_engine import get_daily_plan

# -------------------------------------------------
# Login Check
# -------------------------------------------------

if not is_logged_in():

    st.warning("Please login first.")

    st.stop()

# -------------------------------------------------
# Load Profile
# -------------------------------------------------

profile = get_profile(current_farmer())

context = build_context()

# -------------------------------------------------
# Page Config
# -------------------------------------------------

st.set_page_config(
    page_title="Smart Agriculture Platform",
    page_icon="🌾",
    layout="wide"
)

# -------------------------------------------------
# Header
# -------------------------------------------------

st.markdown(f"""
# 🌾 Smart Agriculture AI Platform

### Welcome **{profile["farmer_name"]}** 👋

AI Powered Farm Decision Support System
""")

st.divider()

# -------------------------------------------------
# Top Metrics
# -------------------------------------------------

c1,c2,c3,c4 = st.columns(4)

c1.metric(
    "🌱 Crop",
    profile["crop"] if profile["crop"] else "-"
)

c2.metric(
    "🌍 State",
    profile["state"] if profile["state"] else "-"
)

c3.metric(
    "🚜 Land",
    f'{profile["land_area"]} Acres'
)

health = context.get("health")

if health is None:
    health="Not Available"

c4.metric(
    "❤️ Farm Health",
    health
)

st.divider()

# -------------------------------------------------
# Two Columns
# -------------------------------------------------

left,right = st.columns([2,1])

# ======================================================
# LEFT SIDE
# ======================================================

with left:

    st.subheader("📰 Latest Agriculture Updates")

    st.info("""
🌾 PM-KISAN 20th Installment expected soon.

💧 PMKSY encouraging Micro Irrigation.

🚜 Digital Agriculture Mission expanding AI services.

🌱 Natural Farming Mission launched in multiple states.

📦 Government promoting Farmer Producer Organizations (FPOs).
""")

    st.subheader("🚨 Important Alerts")

    st.warning("""
• Check irrigation schedule this week.

• Monitor crop for early disease symptoms.

• Use soil test before fertilizer application.

• Avoid unnecessary pesticide spraying.
""")

    st.subheader("🎯 Today's AI Recommendations")

    plan = get_daily_plan()

    if plan.strip():

        st.success(plan)

    else:

        st.info("Complete AI modules to receive recommendations.")

# ======================================================
# RIGHT SIDE
# ======================================================

with right:

    st.subheader("🏛 Eligible Schemes")

    schemes=context.get("schemes",[])

    if len(schemes)==0:

        st.info("No schemes found.")

    else:

        for scheme in schemes[:3]:

            st.success(f"""
**{scheme["Scheme_Name"]}**

💰 {scheme["Benefit"]}

🏷 Subsidy : {scheme["Subsidy"]}
""")

    st.subheader("📈 Market")

    st.metric(
        "Sugarcane MSP",
        "₹340/q"
    )

    st.metric(
        "Rice MSP",
        "₹2300/q"
    )

st.divider()

# -------------------------------------------------
# Government Missions
# -------------------------------------------------

st.subheader("🇮🇳 Government Agriculture Missions")

a,b,c = st.columns(3)

with a:

    st.info("""
### 🌾 PM-KISAN

Income support

₹6000/year
""")

with b:

    st.info("""
### 🌱 PMFBY

Crop Insurance

Natural disaster protection
""")

with c:

    st.info("""
### 💧 PMKSY

Micro Irrigation

Water conservation
""")

st.divider()

# -------------------------------------------------
# Quick Actions
# -------------------------------------------------

st.subheader("⚡ Quick Access")

q1,q2,q3,q4 = st.columns(4)

with q1:
    st.page_link(
        "pages/2_Disease_Detection.py",
        label="🌿 Disease Detection"
    )

with q2:
    st.page_link(
        "pages/3_Fertilizer.py",
        label="🧪 Fertilizer"
    )

with q3:
    st.page_link(
        "pages/4_Yield_Prediction.py",
        label="🌾 Yield Prediction"
    )

with q4:
    st.page_link(
        "pages/8_AI_Assistant.py",
        label="🤖 AI Assistant"
    )

st.divider()

st.caption(
    "Smart Agriculture AI Platform • Government Schemes • AI Decision Engine • Weather • Disease Detection • Yield Prediction"
)