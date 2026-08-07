import streamlit as st

from utils.yield_predict import predict_yield

from utils.auth import is_logged_in, current_farmer
from utils.profile_manager import get_profile

from utils.ai_data_manager import save_yield
from utils.session_manager import save_prediction
from utils.farmer_memory import save_memory

# =====================================================
# Login Check
# =====================================================

if not is_logged_in():

    st.warning("⚠ Please login first.")

    st.stop()

profile = get_profile(current_farmer())

# =====================================================
# Page Config
# =====================================================

st.set_page_config(

    page_title="Crop Yield Prediction",

    page_icon="🌾",

    layout="wide"

)

st.title("🌾 AI Crop Yield Prediction")

st.write(
    "Predict crop yield using your registered farm profile."
)

st.divider()

# =====================================================
# Farmer Profile
# =====================================================

st.info(f"""
### 👨‍🌾 Registered Farm

**Farmer:** {profile["farmer_name"]}

**State:** {profile["state"]}

**District:** {profile["district"]}

**Crop:** {profile["crop"]}

**Soil:** {profile["soil_type"]}

**Land Area:** {profile["land_area"]} Acres
""")

crop = profile["crop"]
state = profile["state"]
soil = profile["soil_type"]

# =====================================================
# Inputs
# =====================================================

col1, col2 = st.columns(2)

with col1:

    rainfall = st.slider(
        "Rainfall (mm)",
        300,
        1800,
        900
    )

    temperature = st.slider(
        "Temperature (°C)",
        10,
        45,
        28
    )

with col2:

    area = st.number_input(
        "Cultivated Area (Hectare)",
        0.1,
        500.0,
        max(float(profile["land_area"]), 0.1)
    )

st.divider()

# =====================================================
# Prediction
# =====================================================

if st.button("🌾 Predict Yield", use_container_width=True):

    with st.spinner("Running AI Yield Prediction..."):

        yield_prediction, production = predict_yield(

            crop,
            state,
            soil,
            rainfall,
            temperature,
            area

        )

    prices = {

        "Rice":22000,
        "Wheat":21000,
        "Maize":18000,
        "Cotton":65000,
        "Sugarcane":3500,
        "Soybean":45000,
        "Tomato":12000,
        "Potato":15000,
        "Onion":18000,
        "Millet":28000

    }

    price = prices.get(crop,20000)

    revenue = production * price

    # =====================================================
    # Save to Session Manager
    # =====================================================

    save_prediction("yield", yield_prediction)
    save_prediction("production", production)
    save_prediction("revenue", revenue)

    # =====================================================
    # Save Database
    # =====================================================

    save_yield(

        current_farmer(),

        yield_prediction,

        production,

        revenue

    )

    # =====================================================
    # Save AI Memory
    # =====================================================

    save_memory(

        farmer_id=current_farmer(),

        crop=crop,

        yield_prediction=yield_prediction,

        production=production,

        revenue=revenue

    )

    # =====================================================
    # Results
    # =====================================================

    st.success("✅ Yield Prediction Completed")

    c1, c2, c3 = st.columns(3)

    c1.metric(

        "Yield",

        f"{yield_prediction:.2f} ton/ha"

    )

    c2.metric(

        "Production",

        f"{production:.2f} ton"

    )

    c3.metric(

        "Estimated Revenue",

        f"₹ {revenue:,.0f}"

    )

    st.divider()

    if yield_prediction >= 6:

        st.success("🟢 Excellent yield expected.")

    elif yield_prediction >= 4:

        st.info("🟡 Average yield expected.")

    else:

        st.warning("🔴 Low yield expected. Improve irrigation and nutrient management.")

    st.balloons()