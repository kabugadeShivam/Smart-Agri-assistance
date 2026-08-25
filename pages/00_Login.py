import streamlit as st

from utils.auth import (
    authenticate,
    is_logged_in,
    current_farmer,
    logout
)

from utils.database import register_farmer


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Smart Agri AI",
    page_icon="🌾",
    layout="centered"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    .main-title {
        text-align: center;
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        color: #6b7280;
        font-size: 17px;
        margin-bottom: 25px;
    }

    .feature {
        padding: 15px;
        border-radius: 12px;
        background: #f5f7f5;
        text-align: center;
        margin-bottom: 10px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# LOGGED-IN USER
# ============================================================

if is_logged_in():

    st.markdown(
        '<div class="main-title">🌾 Smart Agri AI</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">AI-powered digital farming assistant</div>',
        unsafe_allow_html=True
    )

    st.success(
        f"👨‍🌾 Logged in as Farmer: {current_farmer()}"
    )

    st.divider()

    st.info(
        """
        Your Smart Agri AI system is ready.

        🌿 Disease Detection  
        🧪 Fertilizer Recommendation  
        🌾 Yield Prediction  
        🌦 Weather Analysis  
        🏛 Government Schemes  
        📈 Market Intelligence  
        🤖 AI Farm Advisor
        """
    )

    if st.button(
        "🚪 Logout",
        use_container_width=True,
        key="logout_button"
    ):

        logout()

        st.success(
            "You have been logged out."
        )

        st.rerun()

    st.stop()


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="main-title">🌾 Smart Agri AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Your intelligent digital farming assistant</div>',
    unsafe_allow_html=True
)


# ============================================================
# FEATURES
# ============================================================

c1, c2, c3 = st.columns(3)

with c1:

    st.markdown(
        """
        <div class="feature">
        🌿<br>
        <b>Disease AI</b><br>
        Detect crop diseases
        </div>
        """,
        unsafe_allow_html=True
    )


with c2:

    st.markdown(
        """
        <div class="feature">
        🌾<br>
        <b>Yield AI</b><br>
        Predict crop production
        </div>
        """,
        unsafe_allow_html=True
    )


with c3:

    st.markdown(
        """
        <div class="feature">
        🏛<br>
        <b>Government Schemes</b><br>
        Find eligible schemes
        </div>
        """,
        unsafe_allow_html=True
    )


st.divider()


# ============================================================
# LOGIN / REGISTER
# ============================================================

login_tab, register_tab = st.tabs(
    [
        "🔐 Login",
        "📝 Register"
    ]
)


# ============================================================
# LOGIN
# ============================================================

with login_tab:

    st.subheader("🔐 Farmer Login")

    mobile = st.text_input(
        "📱 Mobile Number",
        max_chars=10,
        key="login_mobile"
    )

    password = st.text_input(
        "🔑 Password",
        type="password",
        key="login_password"
    )

    if st.button(
        "🚀 Login",
        use_container_width=True,
        key="login_button"
    ):

        if not mobile.strip():

            st.warning(
                "Please enter your mobile number."
            )

        elif not password.strip():

            st.warning(
                "Please enter your password."
            )

        elif not mobile.isdigit():

            st.warning(
                "Mobile number must contain digits only."
            )

        elif len(mobile) != 10:

            st.warning(
                "Mobile number must contain exactly 10 digits."
            )

        else:

            try:

                success = authenticate(
                    mobile,
                    password
                )

                if success:

                    st.success(
                        "✅ Login successful!"
                    )

                    st.rerun()

                else:

                    st.error(
                        "❌ Invalid mobile number or password."
                    )

            except Exception as e:

                st.error(
                    f"❌ Login error: {e}"
                )


# ============================================================
# REGISTRATION
# ============================================================

with register_tab:

    st.subheader("📝 Create Farmer Account")

    name = st.text_input(
        "👨‍🌾 Farmer Name",
        key="register_name"
    )

    register_mobile = st.text_input(
        "📱 Mobile Number",
        max_chars=10,
        key="register_mobile"
    )

    register_password = st.text_input(
        "🔐 Password",
        type="password",
        key="register_password"
    )

    confirm_password = st.text_input(
        "🔐 Confirm Password",
        type="password",
        key="register_confirm_password"
    )

    st.markdown("### 🌱 Farm Information")

    state = st.text_input(
        "📍 State",
        key="register_state"
    )

    district = st.text_input(
        "🏙 District",
        key="register_district"
    )

    village = st.text_input(
        "🏡 Village",
        key="register_village"
    )

    crop = st.text_input(
        "🌾 Main Crop",
        key="register_crop"
    )

    land_area = st.number_input(
        "📐 Land Area (hectares)",
        min_value=0.0,
        max_value=5000.0,
        value=1.0,
        step=0.1,
        key="register_land_area"
    )

    soil_type = st.selectbox(
        "🌱 Soil Type",
        [
            "Black Soil",
            "Red Soil",
            "Alluvial Soil",
            "Laterite Soil",
            "Sandy Soil",
            "Loamy Soil",
            "Other"
        ],
        key="register_soil_type"
    )

    irrigation = st.selectbox(
        "💧 Irrigation",
        [
            "Rainfed",
            "Drip",
            "Sprinkler",
            "Canal",
            "Borewell",
            "Other"
        ],
        key="register_irrigation"
    )

    farming_type = st.selectbox(
        "🚜 Farming Type",
        [
            "Conventional",
            "Organic",
            "Mixed"
        ],
        key="register_farming_type"
    )

    age = st.number_input(
        "🎂 Age",
        min_value=18,
        max_value=100,
        value=30,
        step=1,
        key="register_age"
    )

    gender = st.selectbox(
        "Gender",
        [
            "Male",
            "Female",
            "Other"
        ],
        key="register_gender"
    )

    annual_income = st.number_input(
        "💰 Annual Farm Income (₹)",
        min_value=0.0,
        max_value=100000000.0,
        value=100000.0,
        step=10000.0,
        key="register_income"
    )

    fpo_member = st.selectbox(
        "🤝 FPO Member?",
        [
            "Yes",
            "No"
        ],
        key="register_fpo"
    )

    if st.button(
        "🌱 Create Farmer Account",
        use_container_width=True,
        key="register_button"
    ):

        if not name.strip():

            st.warning(
                "Please enter farmer name."
            )

        elif not register_mobile.strip():

            st.warning(
                "Please enter mobile number."
            )

        elif not register_mobile.isdigit():

            st.warning(
                "Mobile number must contain digits only."
            )

        elif len(register_mobile) != 10:

            st.warning(
                "Mobile number must contain exactly 10 digits."
            )

        elif not register_password.strip():

            st.warning(
                "Please enter a password."
            )

        elif len(register_password) < 4:

            st.warning(
                "Password should contain at least 4 characters."
            )

        elif register_password != confirm_password:

            st.error(
                "❌ Passwords do not match."
            )

        else:

            try:

                farmer_id = register_farmer(

                    farmer_name=name.strip(),

                    mobile=register_mobile,

                    password=register_password,

                    state=state.strip(),

                    district=district.strip(),

                    village=village.strip(),

                    crop=crop.strip(),

                    land_area=land_area,

                    soil_type=soil_type,

                    irrigation=irrigation,

                    farming_type=farming_type,

                    age=age,

                    gender=gender,

                    annual_income=annual_income,

                    fpo_member=fpo_member

                )

                if farmer_id:

                    st.success(
                        "✅ Farmer account created successfully!"
                    )

                    st.info(
                        f"🆔 Your Farmer ID is: **{farmer_id}**"
                    )

                    st.info(
                        "You can now go to the Login tab."
                    )

                else:

                    st.error(
                        "❌ Registration failed. "
                        "This mobile number may already be registered."
                    )

            except Exception as e:

                st.error(
                    f"❌ Registration error: {e}"
                )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "🌾 Smart Agri AI | AI-powered agriculture decision support system"
)