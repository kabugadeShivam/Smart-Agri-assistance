import streamlit as st

from utils.scheme_matcher import match_schemes
from utils.scheme_ai import generate_scheme_advice

# ======================================================
# Page Configuration
# ======================================================

st.set_page_config(
    page_title="Government Scheme Matcher",
    page_icon="🏛",
    layout="wide"
)

# ======================================================
# Header
# ======================================================

st.title("🏛 AI Government Scheme Matcher")

st.write("""
Find Central and State Government Agriculture Schemes
that match your farming profile using AI.
""")

st.divider()

# ======================================================
# Farmer Profile
# ======================================================

col1, col2 = st.columns(2)

with col1:

    state = st.selectbox(
        "State",
        [
            "Maharashtra",
            "Punjab",
            "Haryana",
            "Gujarat",
            "Rajasthan",
            "Uttar Pradesh",
            "Madhya Pradesh",
            "Karnataka",
            "Tamil Nadu",
            "Telangana",
            "Andhra Pradesh"
        ]
    )

    crop = st.selectbox(
        "Crop",
        [
            "Rice",
            "Wheat",
            "Maize",
            "Cotton",
            "Sugarcane",
            "Tomato",
            "Onion",
            "Potato",
            "Soybean"
        ]
    )

    land = st.number_input(
        "Land Size (Acres)",
        min_value=0.5,
        max_value=500.0,
        value=2.0
    )

with col2:

    category = st.selectbox(
        "Farmer Category",
        [
            "Marginal Farmer",
            "Small Farmer",
            "Medium Farmer",
            "Large Farmer"
        ]
    )

    need = st.selectbox(
        "Primary Need",
        [
            "Loan",
            "Subsidy",
            "Machinery",
            "Irrigation",
            "Cold Storage",
            "Solar Pump",
            "Organic Farming",
            "Insurance",
            "FPO",
            "Warehouse"
        ]
    )

st.divider()

# ======================================================
# Search
# ======================================================

if st.button("🚀 Find My Schemes", use_container_width=True):

    profile = {

        "state": state,
        "crop": crop,
        "land": land,
        "category": category,
        "need": need

    }

    with st.spinner("🔍 Searching Government Schemes..."):

        schemes = match_schemes(
            state=state,
            crop=crop,
            land_area=land,
            need=need
        )

    # ----------------------------
    # Debug (remove later)
    # ----------------------------

    st.write("Matched Schemes:", len(schemes))

    # ----------------------------
    # No Match
    # ----------------------------

    if len(schemes) == 0:

        st.warning("❌ No matching schemes found.")

        st.stop()

    # ----------------------------
    # Results
    # ----------------------------

    st.success(f"✅ Found {len(schemes)} Matching Schemes")

    st.subheader("🏛 Eligible Government Schemes")

    for scheme in schemes:

        score = scheme.get("Score", 0)

        with st.expander(
            f"{scheme['Scheme_Name']} ⭐ Score {score}"
        ):

            st.write("**Scheme Type:**", scheme["Type"])

            st.write("**State:**", scheme["State"])

            st.write("**Benefit:**", scheme["Benefit"])

            st.write("**Subsidy:**", scheme["Subsidy"])

            st.write("**Eligibility:**")

            st.info(scheme["Eligibility"])

            st.write("**Required Documents:**")

            st.write(scheme["Required_Documents"])

            st.write("**Apply At:**")

            st.write(scheme["Apply_At"])

            st.write("**Official Website:**")

            st.write(scheme["Official_Website"])

    st.divider()

    # ======================================================
    # AI Recommendation
    # ======================================================

    st.subheader("🤖 AI Recommendation")

    with st.spinner("Generating personalized advice..."):

        advice = generate_scheme_advice(
            profile,
            schemes
        )

    st.markdown(advice)