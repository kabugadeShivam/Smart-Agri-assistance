import streamlit as st

from utils.auth import is_logged_in, current_farmer
from utils.profile_manager import get_profile

from utils.ai_engine.context_builder import build_context
from utils.ai_engine.decision_engine import generate_decisions
from utils.ai_engine.recommendation_engine import get_daily_plan

from utils.pdf_report import create_report

# ==========================================================
# LOGIN
# ==========================================================

if not is_logged_in():

    st.warning("⚠ Please login first.")

    st.stop()

# ==========================================================
# LOAD PROFILE
# ==========================================================

profile = get_profile(current_farmer())

context = build_context()

decisions = generate_decisions()

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(

    page_title="Smart AI Farm Advisor",

    page_icon="🤖",

    layout="wide"

)

st.title("🤖 Smart AI Farm Advisor")

st.caption(
    "Unified AI Decision Support System"
)

# ==========================================================
# FARMER PROFILE
# ==========================================================

st.subheader("👨‍🌾 Farmer Profile")

c1,c2,c3,c4 = st.columns(4)

c1.metric("Farmer", profile["farmer_name"])

c2.metric("State", profile["state"])

c3.metric("Crop", profile["crop"])

c4.metric("Land", f"{profile['land_area']} Acres")

st.divider()

# ==========================================================
# CURRENT AI STATUS
# ==========================================================

st.subheader("📊 AI Farm Analysis")

m1,m2,m3,m4 = st.columns(4)

m1.metric(
    "Disease",
    str(context.get("disease","Healthy")).replace("_"," ")
)

m2.metric(
    "Fertilizer",
    context.get("fertilizer","-")
)

m3.metric(
    "Yield",
    f"{context.get('yield',0):.2f} t/ha"
    if context.get("yield") is not None
    else "-"
)

m4.metric(
    "Revenue",
    f"₹ {context.get('revenue',0):,.0f}"
    if context.get("revenue") is not None
    else "-"
)

# ==========================================================
# WEATHER
# ==========================================================

weather = context.get("weather")

if weather:

    st.divider()

    st.subheader("🌦 Weather")

    w1,w2,w3 = st.columns(3)

    w1.metric(
        "Temperature",
        f"{weather.get('temperature','-')} °C"
    )

    w2.metric(
        "Humidity",
        f"{weather.get('humidity','-')} %"
    )

    w3.metric(
        "Condition",
        weather.get("weather","-")
    )

# ==========================================================
# FARM HEALTH
# ==========================================================

farm_health = context.get("farm_health",100)

st.divider()

st.subheader("🌱 Farm Health")

st.progress(min(max(int(farm_health),0),100))

st.metric(

    "Health Score",

    f"{farm_health}/100"

)

if farm_health >= 85:

    st.success("🟢 Excellent Farm Condition")

elif farm_health >= 60:

    st.warning("🟡 Moderate Farm Condition")

else:

    st.error("🔴 Poor Farm Condition")

# ==========================================================
# DAILY PLAN
# ==========================================================

st.divider()

st.subheader("📅 Today's AI Plan")

st.success(get_daily_plan())

# ==========================================================
# AI DECISIONS
# ==========================================================

st.divider()

st.subheader("🧠 AI Decision Engine")

for decision in decisions:

    priority = decision.get("priority","Medium")

    if priority == "Critical":

        st.error(
            f"🔴 {decision['title']}\n\n"
            f"{decision['action']}\n\n"
            f"Reason: {decision.get('reason','')}"
        )

    elif priority == "High":

        st.warning(
            f"🟠 {decision['title']}\n\n"
            f"{decision['action']}\n\n"
            f"Reason: {decision.get('reason','')}"
        )

    elif priority == "Medium":

        st.info(
            f"🟡 {decision['title']}\n\n"
            f"{decision['action']}\n\n"
            f"Reason: {decision.get('reason','')}"
        )

    else:

        st.success(
            f"🟢 {decision['title']}\n\n"
            f"{decision['action']}"
        )

# ==========================================================
# GOVERNMENT SCHEMES
# ==========================================================

schemes = context.get("schemes",[])

if schemes:

    st.divider()

    st.subheader("🏛 Eligible Government Schemes")

    for scheme in schemes[:5]:

        with st.expander(scheme["Scheme_Name"]):

            st.write(f"**Benefit:** {scheme['Benefit']}")

            st.write(f"**Subsidy:** {scheme['Subsidy']}")

            st.write(f"**Eligibility:** {scheme['Eligibility']}")

            st.write(f"**Apply At:** {scheme['Apply_At']}")

# ==========================================================
# AI CONTEXT
# ==========================================================

st.divider()

with st.expander("🧠 AI Context"):

    st.json(context)

# ==========================================================
# PDF REPORT
# ==========================================================

st.divider()

st.subheader("📄 Smart Farm Report")

if st.button("Generate PDF Report", use_container_width=True):

    create_report(

        "farm_report.pdf",

        context.get("fertilizer"),

        context.get("disease"),

        context.get("confidence"),

        context.get("weather"),

        context.get("yield"),

        context.get("production"),

        context.get("revenue"),

        [d["action"] for d in decisions],

        farm_health

    )

    with open("farm_report.pdf","rb") as pdf:

        st.download_button(

            "⬇ Download Report",

            pdf,

            "Smart_Agri_Report.pdf",

            "application/pdf"

        )

    st.success("✅ Report Generated Successfully")