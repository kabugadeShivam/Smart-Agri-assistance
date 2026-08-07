import streamlit as st

from utils.farmer_profile import save_farmer, get_farmer

st.set_page_config(
    page_title="Farmer Profile",
    page_icon="👨‍🌾",
    layout="wide"
)

st.title("👨‍🌾 Farmer Profile")

st.write("Fill your profile once. All AI modules will automatically use this information.")

st.divider()

# -------------------------------
# Search Existing Farmer
# -------------------------------

mobile_search = st.text_input("📱 Mobile Number")

existing = None

if mobile_search:
    existing = get_farmer(mobile_search)

    if existing:
        st.success("Farmer profile found.")
    else:
        st.info("No profile found. Create a new one.")

st.divider()

# -------------------------------
# Profile Form
# -------------------------------

with st.form("profile_form"):

    farmer_name = st.text_input(
        "Farmer Name",
        value=existing["farmer_name"] if existing else ""
    )

    mobile = st.text_input(
        "Mobile",
        value=mobile_search
    )

    state = st.text_input(
        "State",
        value=existing["state"] if existing else ""
    )

    district = st.text_input(
        "District",
        value=existing["district"] if existing else ""
    )

    village = st.text_input(
        "Village",
        value=existing["village"] if existing else ""
    )

    crop = st.text_input(
        "Primary Crop",
        value=existing["crop"] if existing else ""
    )

    land_area = st.number_input(
        "Land Area (Acres)",
        min_value=0.0,
        value=float(existing["land_area"]) if existing else 0.0
    )

    soil_type = st.selectbox(
        "Soil Type",
        [
            "Black",
            "Red",
            "Alluvial",
            "Laterite",
            "Loamy"
        ],
        index=0
    )

    irrigation = st.selectbox(
        "Irrigation",
        [
            "Yes",
            "No"
        ],
        index=0
    )

    farming_type = st.selectbox(
        "Farming Type",
        [
            "Conventional",
            "Organic",
            "Natural"
        ],
        index=0
    )

    age = st.number_input(
        "Age",
        min_value=18,
        max_value=100,
        value=int(existing["age"]) if existing else 25
    )

    gender = st.selectbox(
        "Gender",
        [
            "Male",
            "Female",
            "Other"
        ],
        index=0
    )

    annual_income = st.number_input(
        "Annual Income (₹)",
        min_value=0.0,
        value=float(existing["annual_income"]) if existing else 0.0
    )

    fpo_member = st.selectbox(
        "FPO Member",
        [
            "Yes",
            "No"
        ],
        index=0
    )

    submitted = st.form_submit_button("💾 Save Profile")

# -------------------------------
# Save
# -------------------------------

if submitted:

    save_farmer(
        farmer_name,
        mobile,
        state,
        district,
        village,
        crop,
        land_area,
        soil_type,
        irrigation,
        farming_type,
        age,
        gender,
        annual_income,
        fpo_member
    )

    st.success("✅ Farmer Profile Saved Successfully")
    st.balloons()