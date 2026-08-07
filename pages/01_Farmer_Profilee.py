import streamlit as st

from utils.auth import is_logged_in, current_farmer
from utils.profile_manager import save_profile, get_profile

# ==========================================
# Login Check
# ==========================================

if not is_logged_in():

    st.warning("Please login first.")

    st.stop()

# ==========================================
# Page
# ==========================================

st.set_page_config(

    page_title="Farmer Profile",

    page_icon="👨‍🌾",

    layout="wide"

)

st.title("👨‍🌾 Farmer Profile")

profile = get_profile(current_farmer())

# Already Exists

if profile:

    st.success("Profile already created.")

    st.write(profile)

    st.stop()

# ==========================================
# Form
# ==========================================

with st.form("profile_form"):

    col1, col2 = st.columns(2)

    with col1:

        state = st.selectbox(

            "State",

            [

                "Maharashtra",

                "Gujarat",

                "Punjab",

                "Karnataka",

                "Tamil Nadu",

                "Madhya Pradesh",

                "Other"

            ]

        )

        district = st.text_input("District")

        village = st.text_input("Village")

        land = st.number_input(

            "Land Area (Acres)",

            0.5,

            1000.0,

            1.0

        )

        crop = st.text_input("Main Crop")

    with col2:

        soil = st.selectbox(

            "Soil Type",

            [

                "Black",

                "Red",

                "Loamy",

                "Clay",

                "Sandy"

            ]

        )

        irrigation = st.selectbox(

            "Irrigation",

            [

                "Drip",

                "Sprinkler",

                "Flood",

                "Rainfed"

            ]

        )

        water = st.selectbox(

            "Water Source",

            [

                "Borewell",

                "Canal",

                "River",

                "Rainwater"

            ]

        )

        latitude = st.number_input(

            "Latitude",

            value=0.0

        )

        longitude = st.number_input(

            "Longitude",

            value=0.0

        )

    submitted = st.form_submit_button(

        "💾 Save Profile"

    )

if submitted:

    save_profile(

        current_farmer(),

        state,

        district,

        village,

        land,

        soil,

        irrigation,

        water,

        crop,

        latitude,

        longitude

    )

    st.success("Profile Saved Successfully!")

    st.rerun()