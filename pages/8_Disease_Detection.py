import streamlit as st
from PIL import Image

from utils.disease_predict import predict_disease
from utils.disease_info import DISEASE_INFO

from utils.auth import (
    is_logged_in,
    current_farmer
)

from utils.profile_manager import get_profile

from utils.ai_data_manager import save_disease

from utils.session_manager import save_prediction

from utils.farmer_memory import save_memory

# ============================================================
# LOGIN CHECK
# ============================================================

if not is_logged_in():

    st.warning("⚠ Please login first.")

    st.stop()

# ============================================================
# LOAD PROFILE
# ============================================================

profile = get_profile(current_farmer())

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="🌿 AI Disease Detection",
    page_icon="🌿",
    layout="wide"
)

# ============================================================
# PROFESSIONAL CSS
# ============================================================

st.markdown("""
<style>

.block-container{
    padding-top:1rem;
    padding-bottom:2rem;
}

.hero{
    background:linear-gradient(90deg,#0f766e,#16a34a,#22c55e);
    padding:28px;
    border-radius:18px;
    color:white;
    box-shadow:0px 5px 18px rgba(0,0,0,.18);
    margin-bottom:20px;
}

.metric-card{
    background:#ffffff;
    border-radius:15px;
    padding:18px;
    border:1px solid #EAEAEA;
    box-shadow:0px 2px 10px rgba(0,0,0,.05);
}

.upload-box{
    background:#f8fafc;
    padding:18px;
    border-radius:15px;
    border:1px solid #E5E7EB;
}

</style>
""", unsafe_allow_html=True)

# ============================================================
# HERO
# ============================================================

st.markdown("""

<div class="hero">

<h1>🌿 AI Plant Disease Detection</h1>

<p style="font-size:18px">

Upload a clear crop leaf image and let our Deep Learning AI instantly detect plant diseases,
estimate confidence, calculate farm health, and provide treatment & prevention recommendations.

</p>

</div>

""", unsafe_allow_html=True)

# ============================================================
# FARMER INFORMATION
# ============================================================

st.subheader("👨‍🌾 Registered Farmer")

a,b,c,d = st.columns(4)

a.metric(
    "Farmer ID",
    current_farmer()
)

b.metric(
    "State",
    profile["state"] if profile["state"] else "-"
)

c.metric(
    "Crop",
    profile["crop"] if profile["crop"] else "-"
)

d.metric(
    "Soil",
    profile["soil_type"] if profile["soil_type"] else "-"
)

st.divider()

# ============================================================
# TWO COLUMN LAYOUT
# ============================================================

left,right = st.columns([1.2,1])

with left:

    st.markdown("### 📤 Upload Leaf Image")

    uploaded_file = st.file_uploader(
        "Choose an Image",
        type=["jpg","jpeg","png"]
    )

    st.caption(
        "Recommended: Clear close-up image captured in natural daylight."
    )

with right:

    st.markdown("### 🤖 AI Analysis")

    st.success("✔ Disease Classification")

    st.success("✔ Confidence Score")

    st.success("✔ Farm Health Score")

    st.success("✔ Treatment Suggestion")

    st.success("✔ Prevention Guide")

    st.success("✔ Farmer AI Memory")

st.divider()

# ============================================================
# IMAGE PREVIEW
# ============================================================

detect = False

if uploaded_file is not None:

    original = Image.open(uploaded_file)

    image = original.convert("RGB")

    col1,col2 = st.columns([1.2,1])

    with col1:

        st.image(
            image,
            use_container_width=True
        )

    with col2:

        st.subheader("📄 Image Details")

        width,height = image.size

        st.metric(
            "Resolution",
            f"{width} × {height}"
        )

        st.write(
            "**Filename:**",
            uploaded_file.name
        )

        st.write(
            "**Format:**",
            original.format
        )

        st.write(
            "**Mode:**",
            image.mode
        )

        st.info(
            "The AI model will analyse the uploaded leaf and estimate disease severity."
        )

        detect = st.button(
            "🚀 Run AI Diagnosis",
            use_container_width=True
        )

# ============================================================
# AI PREDICTION
# ============================================================

if detect:

    with st.spinner("🧠 AI is analysing your crop..."):

        disease, confidence = predict_disease(image)

    disease_lower = disease.lower()

    if "healthy" in disease_lower:

        farm_health = 100
        severity = "🟢 Healthy"
        risk = "Very Low"

    elif confidence >= 95:

        farm_health = 35
        severity = "🔴 Critical"
        risk = "Very High"

    elif confidence >= 85:

        farm_health = 55
        severity = "🟠 Severe"
        risk = "High"

    elif confidence >= 70:

        farm_health = 72
        severity = "🟡 Moderate"
        risk = "Medium"

    else:

        farm_health = 85
        severity = "🟢 Mild"
        risk = "Low"

    save_prediction("disease", disease)
    save_prediction("confidence", confidence)
    save_prediction("farm_health", farm_health)

    save_disease(
        current_farmer(),
        disease,
        confidence
    )

    save_memory(
        farmer_id=current_farmer(),
        disease=disease,
        confidence=confidence,
        farm_health=farm_health
    )

    st.success("✅ AI Diagnosis Completed Successfully")
        st.divider()

    # ============================================================
    # RESULT METRICS
    # ============================================================

    st.subheader("📊 AI Diagnosis Summary")

    m1, m2, m3, m4 = st.columns(4)

    m1.metric(
        "Disease",
        disease.replace("_", " ")
    )

    m2.metric(
        "Confidence",
        f"{confidence:.2f}%"
    )

    m3.metric(
        "Farm Health",
        f"{farm_health}/100"
    )

    m4.metric(
        "Risk Level",
        risk
    )

    # ============================================================
    # CONFIDENCE BAR
    # ============================================================

    st.divider()

    st.subheader("🎯 Prediction Confidence")

    st.progress(confidence / 100)

    if confidence >= 95:

        st.success("Very high confidence prediction.")

    elif confidence >= 85:

        st.info("High confidence prediction.")

    elif confidence >= 70:

        st.warning("Moderate confidence. Consider uploading another clear image for verification.")

    else:

        st.error("Low confidence prediction. Capture a clearer image under good lighting.")

    # ============================================================
    # FARM HEALTH DASHBOARD
    # ============================================================

    st.divider()

    left, right = st.columns(2)

    with left:

        st.subheader("🌱 Farm Health")

        st.progress(farm_health / 100)

        st.metric(
            "Health Score",
            f"{farm_health}/100"
        )

    with right:

        st.subheader("🚨 Disease Severity")

        st.markdown(f"## {severity}")

        st.write(f"Estimated Risk Level : **{risk}**")

    # ============================================================
    # TREATMENT & PREVENTION
    # ============================================================

    st.divider()

    if disease in DISEASE_INFO:

        info = DISEASE_INFO[disease]

        t1, t2 = st.columns(2)

        with t1:

            st.subheader("💊 Recommended Treatment")

            st.success(info["Treatment"])

        with t2:

            st.subheader("🛡 Prevention")

            st.info(info["Prevention"])

    else:

        st.warning(
            "Treatment information is not available for this disease."
        )

    # ============================================================
    # AI RECOMMENDATIONS
    # ============================================================

    st.divider()

    st.subheader("🤖 AI Recommendations")

    recommendations = []

    if "healthy" in disease_lower:

        recommendations.extend([
            "Continue current crop management practices.",
            "Maintain balanced fertilization.",
            "Monitor crop weekly.",
            "Keep irrigation schedule consistent."
        ])

    else:

        recommendations.extend([
            "Start treatment immediately.",
            "Inspect nearby plants for similar symptoms.",
            "Remove severely infected leaves.",
            "Avoid overhead irrigation until recovery.",
            "Monitor crop every 2–3 days.",
            "Capture another image after treatment to compare improvement."
        ])

    for i, rec in enumerate(recommendations, start=1):

        st.write(f"✅ {i}. {rec}")

    # ============================================================
    # NEXT ACTIONS
    # ============================================================

    st.divider()

    st.subheader("📌 Recommended Next Steps")

    n1, n2, n3 = st.columns(3)

    with n1:

        st.info(
            """
### 🌾 Fertilizer

Open the Fertilizer Recommendation module to identify the most suitable fertilizer.
"""
        )

    with n2:

        st.info(
            """
### 📈 Yield Prediction

Estimate production, expected revenue and profitability.
"""
        )

    with n3:

        st.info(
            """
### 🤖 AI Advisor

Ask questions about this disease, treatment and government schemes.
"""
        )

    # ============================================================
    # FINAL STATUS
    # ============================================================

    st.divider()

    st.success("🌿 Disease analysis has been successfully saved to your Smart Farm Profile.")

    st.balloons()