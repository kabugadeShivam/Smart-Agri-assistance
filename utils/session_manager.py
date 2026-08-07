import streamlit as st

# =====================================================
# Initialize AI Memory
# =====================================================

DEFAULT_MEMORY = {
    "disease": None,
    "confidence": None,

    "fertilizer": None,

    "yield": None,
    "production": None,
    "revenue": None,

    "weather": None,

    "market": None,

    "schemes": None,

    "farm_health": None,

    "last_prediction": None
}


# =====================================================
# Initialize Session
# =====================================================

def initialize_session():

    if "ai_memory" not in st.session_state:

        st.session_state.ai_memory = DEFAULT_MEMORY.copy()


# =====================================================
# Save Prediction
# =====================================================

def save_prediction(key, value):

    initialize_session()

    st.session_state.ai_memory[key] = value


# =====================================================
# Get Prediction
# =====================================================

def get_prediction(key):

    initialize_session()

    return st.session_state.ai_memory.get(key)


# =====================================================
# Get Complete AI Context
# =====================================================

def get_all_predictions():

    initialize_session()

    return st.session_state.ai_memory


# =====================================================
# Update Multiple Values
# =====================================================

def update_predictions(data: dict):

    initialize_session()

    st.session_state.ai_memory.update(data)


# =====================================================
# Clear AI Memory
# =====================================================

def clear_predictions():

    st.session_state.ai_memory = DEFAULT_MEMORY.copy()