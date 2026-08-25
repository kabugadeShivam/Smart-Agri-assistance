import streamlit as st

from utils.database import get_farmer_by_mobile


# ============================================================
# LOGIN USER
# ============================================================

def login_user(farmer):
    """
    Store the complete farmer profile in Streamlit session.
    """

    if farmer is None:
        return False

    farmer = dict(farmer)

    st.session_state.logged_in = True
    st.session_state.profile = farmer

    # Basic farmer information
    st.session_state.farmer_id = farmer.get("farmer_id")
    st.session_state.farmer_name = farmer.get("farmer_name", "")
    st.session_state.mobile = farmer.get("mobile", "")

    # Location
    st.session_state.state = farmer.get("state", "")
    st.session_state.district = farmer.get("district", "")
    st.session_state.village = farmer.get("village", "")

    # Farm information
    st.session_state.crop = farmer.get("crop", "")
    st.session_state.land_area = farmer.get("land_area", 0)
    st.session_state.soil_type = farmer.get("soil_type", "")
    st.session_state.irrigation = farmer.get("irrigation", "")
    st.session_state.farming_type = farmer.get("farming_type", "")

    # Personal information
    st.session_state.age = farmer.get("age")
    st.session_state.gender = farmer.get("gender", "")

    # Economic information
    st.session_state.annual_income = farmer.get(
        "annual_income",
        0
    )

    st.session_state.fpo_member = farmer.get(
        "fpo_member",
        "No"
    )

    return True


# ============================================================
# AUTHENTICATE FARMER
# ============================================================

def authenticate(mobile, password):
    """
    Authenticate farmer using mobile number and password.

    Returns:
        True  -> successful login
        False -> invalid credentials
    """

    if not mobile or not password:
        return False

    farmer = get_farmer_by_mobile(mobile)

    if farmer is None:
        return False

    farmer_password = farmer.get("password")

    if farmer_password is None:
        return False

    if str(farmer_password) != str(password):
        return False

    return login_user(farmer)


# ============================================================
# CHECK LOGIN
# ============================================================

def is_logged_in():
    """
    Check whether a farmer is currently logged in.
    """

    return st.session_state.get(
        "logged_in",
        False
    )


# ============================================================
# CURRENT FARMER ID
# ============================================================

def current_farmer():
    """
    Return currently logged-in farmer ID.
    """

    return st.session_state.get(
        "farmer_id"
    )


# ============================================================
# CURRENT FARMER PROFILE
# ============================================================

def current_profile():
    """
    Return complete current farmer profile.
    """

    return st.session_state.get(
        "profile",
        {}
    )


# ============================================================
# CURRENT FARMER NAME
# ============================================================

def current_farmer_name():
    """
    Return current farmer name.
    """

    return st.session_state.get(
        "farmer_name",
        ""
    )


# ============================================================
# CURRENT MOBILE
# ============================================================

def current_mobile():
    """
    Return current farmer mobile number.
    """

    return st.session_state.get(
        "mobile",
        ""
    )


# ============================================================
# LOGOUT
# ============================================================

def logout():
    """
    Completely clear the current login session.
    """

    st.session_state.clear()