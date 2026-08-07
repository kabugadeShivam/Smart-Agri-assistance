import streamlit as st

# =====================================================
# Login Session
# =====================================================

def login_user(farmer):
    """
    Stores the complete farmer profile in Streamlit session.
    """

    st.session_state.logged_in = True

    # Master Profile
    st.session_state.profile = dict(farmer)

    # Frequently Used Fields
    st.session_state.farmer_id = farmer["farmer_id"]
    st.session_state.farmer_name = farmer["farmer_name"]
    st.session_state.mobile = farmer["mobile"]

    st.session_state.state = farmer["state"]
    st.session_state.district = farmer["district"]
    st.session_state.village = farmer["village"]

    st.session_state.crop = farmer["crop"]
    st.session_state.land_area = farmer["land_area"]

    st.session_state.soil_type = farmer["soil_type"]
    st.session_state.irrigation = farmer["irrigation"]

    st.session_state.farming_type = farmer["farming_type"]

    st.session_state.age = farmer["age"]
    st.session_state.gender = farmer["gender"]

    st.session_state.annual_income = farmer["annual_income"]
    st.session_state.fpo_member = farmer["fpo_member"]


# =====================================================
# Logout
# =====================================================

def logout():

    st.session_state.clear()


# =====================================================
# Check Login
# =====================================================

def is_logged_in():

    return st.session_state.get("logged_in", False)


# =====================================================
# Current Farmer ID
# =====================================================

def current_farmer():

    return st.session_state.get("farmer_id")


# =====================================================
# Current Farmer Profile
# =====================================================

def current_profile():

    return st.session_state.get("profile", {})