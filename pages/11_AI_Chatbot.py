import streamlit as st

from utils.auth import is_logged_in, current_farmer
from utils.profile_manager import get_profile

from utils.rag import search
from utils.gemini_ai import generate_answer

from utils.ai_engine.context_builder import build_context
from utils.ai_engine.recommendation_engine import get_daily_plan
from utils.ai_engine.decision_engine import generate_decisions

# ======================================================
# LOGIN CHECK
# ======================================================

if not is_logged_in():

    st.warning("⚠ Please login first.")

    st.stop()

profile = get_profile(current_farmer())

# ======================================================
# PAGE CONFIG
# ======================================================

st.set_page_config(

    page_title="Smart Agri AI Assistant",

    page_icon="🌾",

    layout="wide"

)

# ======================================================
# SESSION CHAT
# ======================================================

if "chat_history" not in st.session_state:

    st.session_state.chat_history = []

# ======================================================
# HEADER
# ======================================================

st.title("🌾 Smart Agri AI Assistant")

st.caption(
    "AI Agriculture Copilot powered by Disease Detection, Yield Prediction, Weather Intelligence, Government Schemes and Gemini AI."
)

# ======================================================
# FARMER PROFILE
# ======================================================

st.subheader("👨‍🌾 Current Farmer")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Name", profile["farmer_name"])
c2.metric("State", profile["state"])
c3.metric("Crop", profile["crop"])
c4.metric("Land", f"{profile['land_area']} Acres")

st.divider()

# ======================================================
# TODAY'S PLAN
# ======================================================

st.subheader("🌾 Today's AI Farm Plan")

plan = get_daily_plan()

if plan.strip():

    st.success(plan)

else:

    st.info("No AI recommendation available.")

# ======================================================
# PRIORITIES
# ======================================================

st.subheader("🚨 AI Priorities")

decisions = generate_decisions()

if len(decisions) == 0:

    st.info("No active priority.")

else:

    for item in decisions:

        if item["priority"] == "HIGH":

            st.error(f"🔴 {item['title']}\n\n{item['action']}")

        elif item["priority"] == "MEDIUM":

            st.warning(f"🟡 {item['title']}\n\n{item['action']}")

        else:

            st.info(f"🔵 {item['title']}\n\n{item['action']}")

st.divider()

# ======================================================
# CHAT HISTORY
# ======================================================

st.subheader("💬 Conversation")

for chat in st.session_state.chat_history:

    with st.chat_message(chat["role"]):

        st.markdown(chat["content"])

# ======================================================
# CHAT INPUT
# ======================================================

question = st.chat_input(
    "Ask anything about your farm..."
)

# ======================================================
# ASK AI
# ======================================================

if question:

    st.session_state.chat_history.append({

        "role":"user",

        "content":question

    })

    with st.chat_message("user"):

        st.markdown(question)

    with st.spinner("Searching Agriculture Knowledge..."):

        rag_results = search(question)

    with st.spinner("Thinking like an Agriculture Expert..."):

        answer = generate_answer(question)

    st.session_state.chat_history.append({

        "role":"assistant",

        "content":answer

    })

    with st.chat_message("assistant"):

        st.markdown(answer)

        if len(rag_results) > 0:

            st.divider()

            st.markdown("### 📚 Knowledge Used")

            for result in rag_results:

                with st.expander(result.get("Question","Knowledge")):

                    st.write("**Category**", result.get("Category",""))

                    st.write("**Crop**", result.get("Crop",""))

                    if result.get("Answer"):

                        st.success(result["Answer"])

                    if result.get("Keywords"):

                        st.caption(result["Keywords"])

# ======================================================
# CONTEXT
# ======================================================

st.divider()

with st.expander("🧠 AI Context"):

    st.json(build_context())

# ======================================================
# CLEAR CHAT
# ======================================================

st.divider()

col1, col2 = st.columns([1,4])

with col1:

    if st.button("🗑 Clear Chat"):

        st.session_state.chat_history = []

        st.rerun()

# ======================================================
# FOOTER
# ======================================================

st.divider()

st.caption(
    "Smart Agri AI Assistant • Personalized recommendations using AI, RAG, Farmer Profile, Disease Detection, Yield Prediction, Government Schemes and Decision Engine."
)