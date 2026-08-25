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

    st.warning("⚠️ Please login first.")

    st.stop()


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="AI Plant Disease Detection",
    page_icon="🌿",
    layout="wide"
)


# ============================================================
# LOAD FARMER PROFILE
# ============================================================

farmer_id = current_farmer()

profile = get_profile(farmer_id)


# ============================================================
# SAFE PROFILE VALUES
# ============================================================

def get_profile_value(profile_data, key, index, default="-"):

    try:

        if profile_data is None:
            return default

        # SQLite Row / dictionary
        if hasattr(profile_data, "keys"):

            value = profile_data[key]

        else:

            value = profile_data[index]

        if value is None or str(value).strip() == "":
            return default

        return value

    except (KeyError, IndexError, TypeError):

        return default


# Your farmer_profile table structure:
#
# 0  farmer_id
# 1  farmer_name
# 2  mobile
# 3  state
# 4  district
# 5  village
# 6  crop
# 7  land_area
# 8  soil_type
# 9  irrigation
# 10 farming_type
# 11 age
# 12 gender
# 13 annual_income
# 14 fpo_member
# 15 created_at


farmer_name = get_profile_value(
    profile,
    "farmer_name",
    1
)

state = get_profile_value(
    profile,
    "state",
    3
)

district = get_profile_value(
    profile,
    "district",
    4
)

village = get_profile_value(
    profile,
    "village",
    5
)

crop = get_profile_value(
    profile,
    "crop",
    6
)

soil_type = get_profile_value(
    profile,
    "soil_type",
    8
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    .main-title {
        font-size: 38px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .subtitle {
        font-size: 17px;
        color: #666;
        margin-bottom: 20px;
    }

    .hero {
        padding: 30px;
        border-radius: 18px;
        background: linear-gradient(
            135deg,
            #166534,
            #16a34a
        );
        color: white;
        margin-bottom: 25px;
    }

    .hero h1 {
        color: white;
        margin-bottom: 8px;
    }

    .hero p {
        color: white;
        font-size: 17px;
    }

    .info-card {
        padding: 18px;
        border-radius: 14px;
        border: 1px solid #e5e7eb;
        background-color: #ffffff;
        margin-bottom: 15px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# HERO SECTION
# ============================================================

st.markdown(
    """
    <div class="hero">

        <h1>🌿 AI Plant Disease Detection</h1>

        <p>
        Upload a crop leaf image and let the AI model analyse
        the plant condition, estimate prediction confidence,
        assess farm health and provide treatment guidance.
        </p>

    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# FARMER INFORMATION
# ============================================================

st.subheader("👨‍🌾 Farmer & Farm Information")


c1, c2, c3, c4 = st.columns(4)


with c1:

    st.metric(
        "Farmer",
        str(farmer_name)
    )


with c2:

    st.metric(
        "State",
        str(state)
    )


with c3:

    st.metric(
        "District",
        str(district)
    )


with c4:

    st.metric(
        "Crop",
        str(crop)
    )


st.divider()


# ============================================================
# MAIN INPUT SECTION
# ============================================================

upload_col, feature_col = st.columns(
    [1.4, 1]
)


# ============================================================
# IMAGE UPLOAD
# ============================================================

with upload_col:

    st.subheader("📤 Upload Crop Leaf")

    uploaded_file = st.file_uploader(
        "Choose a JPG, JPEG or PNG image",
        type=[
            "jpg",
            "jpeg",
            "png"
        ],
        help=(
            "For best results, upload a clear close-up "
            "image of the affected leaf."
        )
    )


# ============================================================
# AI FEATURES
# ============================================================

with feature_col:

    st.subheader("🤖 AI Analysis")

    st.success("✅ Disease Classification")

    st.success("✅ Confidence Score")

    st.success("✅ Farm Health Assessment")

    st.success("✅ Treatment Guidance")

    st.success("✅ Prevention Guidance")

    st.success("✅ Farmer AI Memory")


st.divider()


# ============================================================
# DEFAULT DETECT VALUE
# IMPORTANT:
# This prevents NameError: detect is not defined
# ============================================================

detect = False


# ============================================================
# IMAGE PREVIEW
# ============================================================

if uploaded_file is not None:

    try:

        original_image = Image.open(
            uploaded_file
        )

        image = original_image.convert(
            "RGB"
        )

    except Exception as e:

        st.error(
            f"❌ Unable to read the uploaded image: {e}"
        )

        st.stop()


    preview_col, details_col = st.columns(
        [1.4, 1]
    )


    # ========================================================
    # IMAGE
    # ========================================================

    with preview_col:

        st.subheader("🖼️ Image Preview")

        st.image(
            image,
            caption="Uploaded Crop Leaf",
            use_container_width=True
        )


    # ========================================================
    # IMAGE DETAILS
    # ========================================================

    with details_col:

        st.subheader("📋 Image Details")

        width, height = image.size

        st.write(
            f"**File:** {uploaded_file.name}"
        )

        st.write(
            f"**Resolution:** {width} × {height}"
        )

        st.write(
            f"**Format:** {original_image.format or 'Unknown'}"
        )

        st.write(
            f"**Color Mode:** {image.mode}"
        )

        st.info(
            "For better accuracy, use a clear image "
            "with good lighting and minimal background."
        )


    st.divider()


    # ========================================================
    # DETECT BUTTON
    # ========================================================

    detect = st.button(
        "🔍 Run AI Disease Diagnosis",
        use_container_width=True,
        type="primary"
    )


# ============================================================
# NO IMAGE
# ============================================================

else:

    st.info(
        "📷 Upload a crop leaf image above to start AI diagnosis."
    )


# ============================================================
# AI PREDICTION
# ============================================================

if detect:

    # ========================================================
    # PREDICTION
    # ========================================================

    with st.spinner(
        "🧠 AI is analysing the crop leaf..."
    ):

        try:

            disease, confidence = predict_disease(
                image
            )

        except Exception as e:

            st.error(
                "❌ Disease prediction failed."
            )

            st.exception(e)

            st.stop()


    # ========================================================
    # NORMALIZE VALUES
    # ========================================================

    disease = str(disease)

    confidence = float(confidence)

    disease_lower = disease.lower()


    # ========================================================
    # FARM HEALTH SCORE
    # ========================================================

    if "healthy" in disease_lower:

        farm_health = 100

        severity = "🟢 Healthy"

        risk = "Very Low"

    elif confidence >= 95:

        farm_health = 40

        severity = "🔴 Critical"

        risk = "Very High"

    elif confidence >= 85:

        farm_health = 60

        severity = "🟠 Severe"

        risk = "High"

    elif confidence >= 70:

        farm_health = 75

        severity = "🟡 Moderate"

        risk = "Medium"

    else:

        farm_health = 85

        severity = "🟢 Low Confidence"

        risk = "Low"


    # ========================================================
    # SAVE SESSION DATA
    # ========================================================

    save_prediction(
        "disease",
        disease
    )

    save_prediction(
        "confidence",
        confidence
    )

    save_prediction(
        "farm_health",
        farm_health
    )


    # ========================================================
    # SAVE TO PREDICTION DATABASE
    # ========================================================

    try:

        save_disease(
            farmer_id,
            disease,
            confidence
        )

    except Exception as e:

        st.warning(
            f"⚠️ Prediction generated but database save failed: {e}"
        )


    # ========================================================
    # SAVE TO FARMER MEMORY
    # ========================================================

    try:

        save_memory(
            farmer_id=farmer_id,
            crop=crop,
            soil=soil_type,
            disease=disease,
            confidence=confidence,
            farm_health=farm_health
        )

    except Exception as e:

        st.warning(
            f"⚠️ Farmer memory update failed: {e}"
        )


    # ========================================================
    # SUCCESS
    # ========================================================

    st.success(
        "✅ AI Disease Diagnosis Completed Successfully"
    )


    st.divider()


    # ========================================================
    # DIAGNOSIS SUMMARY
    # ========================================================

    st.subheader("📊 AI Diagnosis Summary")


    r1, r2, r3, r4 = st.columns(4)


    with r1:

        st.metric(
            "🌿 Disease",
            disease.replace("_", " ")
        )


    with r2:

        st.metric(
            "🎯 Confidence",
            f"{confidence:.2f}%"
        )


    with r3:

        st.metric(
            "🌱 Farm Health",
            f"{farm_health}/100"
        )


    with r4:

        st.metric(
            "🚨 Risk",
            risk
        )


    # ========================================================
    # CONFIDENCE
    # ========================================================

    st.divider()

    st.subheader("🎯 Prediction Confidence")


    confidence_value = max(
        0.0,
        min(
            confidence / 100,
            1.0
        )
    )


    st.progress(
        confidence_value
    )


    if confidence >= 95:

        st.success(
            "Very high confidence prediction."
        )

    elif confidence >= 85:

        st.info(
            "High confidence prediction."
        )

    elif confidence >= 70:

        st.warning(
            "Moderate confidence. Upload another clear image "
            "if you want additional verification."
        )

    else:

        st.error(
            "Low confidence prediction. Capture a clearer "
            "image with better lighting."
        )


    # ========================================================
    # FARM HEALTH
    # ========================================================

    st.divider()

    health_col1, health_col2 = st.columns(2)


    with health_col1:

        st.subheader("🌱 Farm Health")

        st.progress(
            farm_health / 100
        )

        st.metric(
            "Health Score",
            f"{farm_health}/100"
        )


    with health_col2:

        st.subheader("🚨 Disease Severity")

        st.markdown(
            f"### {severity}"
        )

        st.write(
            f"Estimated risk: **{risk}**"
        )


    # ========================================================
    # DISEASE INFORMATION
    # ========================================================

    st.divider()

    st.subheader(
        "💊 Treatment & Prevention"
    )


    if disease in DISEASE_INFO:

        info = DISEASE_INFO[disease]


        treatment_col, prevention_col = st.columns(2)


        with treatment_col:

            st.markdown(
                "### 💊 Recommended Treatment"
            )

            st.info(
                info.get(
                    "Treatment",
                    "No treatment information available."
                )
            )


        with prevention_col:

            st.markdown(
                "### 🛡 Prevention"
            )

            st.success(
                info.get(
                    "Prevention",
                    "No prevention information available."
                )
            )


    else:

        st.warning(
            "No detailed treatment information is currently "
            "available for this prediction."
        )


    # ========================================================
    # AI RECOMMENDATIONS
    # ========================================================

    st.divider()

    st.subheader(
        "🤖 Recommended Actions"
    )


    if "healthy" in disease_lower:

        recommendations = [

            "Continue the current crop management practices.",

            "Maintain balanced irrigation and fertilization.",

            "Regularly inspect the crop for early symptoms.",

            "Maintain good field hygiene.",

            "Run another diagnosis if new symptoms appear."

        ]

    else:

        recommendations = [

            "Inspect nearby plants for similar symptoms.",

            "Separate or remove severely affected plant material "
            "where appropriate.",

            "Follow the recommended treatment guidance.",

            "Avoid unnecessary overhead irrigation.",

            "Monitor the crop every 2–3 days.",

            "Repeat the AI diagnosis after treatment to compare "
            "the plant condition."

        ]


    for number, recommendation in enumerate(
        recommendations,
        start=1
    ):

        st.write(
            f"**{number}.** {recommendation}"
        )


    # ========================================================
    # NEXT ACTIONS
    # ========================================================

    st.divider()

    st.subheader(
        "📌 Continue Your Farm Analysis"
    )


    action1, action2, action3 = st.columns(3)


    with action1:

        st.info(
            """
**🧪 Fertilizer Recommendation**

Use your farm profile and crop information to determine suitable nutrient management.
"""
        )


    with action2:

        st.info(
            """
**🌾 Yield Prediction**

Estimate expected yield, production and potential revenue.
"""
        )


    with action3:

        st.info(
            """
**🤖 Smart AI Advisor**

Ask questions about disease management, weather, schemes and your farm.
"""
        )


    # ========================================================
    # MEMORY STATUS
    # ========================================================

    st.divider()

    st.success(
        "🧠 This diagnosis has been added to your Farmer AI Memory."
    )


# ============================================================
# INFORMATION FOOTER
# ============================================================

st.divider()

st.caption(
    "🌾 Smart Agri AI • AI-powered crop disease analysis • "
    "Always verify serious disease diagnoses with a qualified "
    "agriculture professional."
)