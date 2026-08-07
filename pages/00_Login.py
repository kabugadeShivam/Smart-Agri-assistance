import streamlit as st

from utils.profile_manager import register_farmer, login
from utils.auth import login_user, is_logged_in

# =====================================================
# Page Config
# =====================================================

st.set_page_config(
    page_title="Smart Agri AI",
    page_icon="🌾",
    layout="wide"
)

# Already logged in
if is_logged_in():

    st.success(f"Welcome back, {st.session_state.farmer_name} 👋")

    st.switch_page("pages/02_Dashboard.py")

# =====================================================
# Header
# =====================================================

st.markdown("""
# 🌾 Smart Agri AI Platform

### Intelligent Farming • AI Advisor • Market Intelligence • Government Schemes
""")

st.divider()

left, right = st.columns([1.2, 1])

# =====================================================
# Left Side
# =====================================================

with left:

    st.image(
        "https://images.unsplash.com/photo-1500937386664-56d1dfef3854?w=900",
        use_container_width=True
    )

    st.markdown("## Why Smart Agri AI?")

    st.success("🌱 Disease Detection")

    st.success("🌾 Yield Prediction")

    st.success("🏛 Government Scheme Matching")

    st.success("📈 Market Intelligence")

    st.success("🤖 AI Agriculture Advisor")

    st.success("📄 AI Farm Reports")

# =====================================================
# Right Side
# =====================================================

with right:

    tabs = st.tabs(["🔐 Login", "📝 Register"])

    # =====================================================
    # LOGIN
    # =====================================================

    with tabs[0]:

        st.subheader("Farmer Login")

        login_mobile = st.text_input(
            "📱 Mobile Number",
            max_chars=10
        )

        if st.button(
            "Login",
            use_container_width=True
        ):

            if len(login_mobile) != 10 or not login_mobile.isdigit():

                st.error("Enter a valid 10-digit mobile number.")

            else:

                farmer = login(login_mobile)

                if farmer:

                    login_user(farmer)

                    st.success(
                        f"Welcome {farmer['farmer_name']} 🌾"
                    )

                    st.rerun()

                else:

                    st.error(
                        "Farmer not found. Please register first."
                    )

    # =====================================================
    # REGISTER
    # =====================================================

    with tabs[1]:

        st.subheader("New Farmer Registration")

        name = st.text_input(
            "👤 Full Name"
        )

        mobile = st.text_input(
            "📱 Mobile Number",
            max_chars=10
        )

        if st.button(
            "Register",
            use_container_width=True
        ):

            if name == "":

                st.warning("Please enter your name.")

            elif len(mobile) != 10 or not mobile.isdigit():

                st.warning("Please enter a valid mobile number.")

            else:

                try:

                    farmer_id = register_farmer(
                        name=name,
                        mobile=mobile
                    )

                    st.success(
                        f"""
Registration Successful 🎉

Farmer ID : {farmer_id}

Please login using your mobile number.
"""
                    )

                except Exception as e:

                    st.error(str(e))

st.divider()

st.caption(
    "© 2026 Smart Agri AI Platform | AI Powered Decision Support for Indian Farmers 🇮🇳"
)