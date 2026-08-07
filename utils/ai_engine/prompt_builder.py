from utils.ai_engine.context_builder import build_context
from utils.ai_engine.history_builder import build_history_context
from utils.ai_engine.decision_engine import generate_decisions
from utils.auth import current_farmer


# =====================================================
# Prompt Builder
# =====================================================

def build_prompt(question):

    farmer_id = current_farmer()

    context = build_context()

    history = build_history_context(farmer_id)

    decisions = generate_decisions()

    farmer = context["farmer"]

    # =====================================================
    # Government Schemes
    # =====================================================

    scheme_text = ""

    schemes = context.get("schemes", [])

    if schemes:

        for i, scheme in enumerate(schemes, start=1):

            scheme_text += f"""
{i}. {scheme.get('Scheme_Name','N/A')}

Benefit:
{scheme.get('Benefit','N/A')}

Subsidy:
{scheme.get('Subsidy','N/A')}

Eligibility:
{scheme.get('Eligibility','N/A')}

Apply At:
{scheme.get('Apply_At','N/A')}

Website:
{scheme.get('Official_Website','N/A')}

------------------------------------------
"""

    else:

        scheme_text = "No matching government schemes."

    # =====================================================
    # AI Decisions
    # =====================================================

    decision_text = ""

    for d in decisions:

        decision_text += f"""

Priority : {d.get('priority')}

Action : {d.get('action')}

Reason : {d.get('reason','')}

---------------------------------------
"""

    # =====================================================
    # Prompt
    # =====================================================

    prompt = f"""

You are SmartAgri AI,
an expert Agriculture Advisor for Indian farmers.

====================================================
FARMER PROFILE
====================================================

Name:
{farmer.get("farmer_name")}

State:
{farmer.get("state")}

District:
{farmer.get("district")}

Village:
{farmer.get("village")}

Crop:
{farmer.get("crop")}

Land:
{farmer.get("land_area")} Acres

Soil:
{farmer.get("soil_type")}

Irrigation:
{farmer.get("irrigation")}

Farming Type:
{farmer.get("farming_type")}

====================================================
CURRENT AI ANALYSIS
====================================================

Disease:
{context.get("disease")}

Confidence:
{context.get("confidence")}

Recommended Fertilizer:
{context.get("fertilizer")}

Expected Yield:
{context.get("yield")}

Expected Production:
{context.get("production")}

Expected Revenue:
{context.get("revenue")}

Weather:
{context.get("weather")}

Market:
{context.get("market")}

Farm Health:
{context.get("farm_health")}

====================================================
AI DECISION ENGINE
====================================================

{decision_text}

====================================================
PREVIOUS FARM HISTORY
====================================================

{history}

====================================================
ELIGIBLE GOVERNMENT SCHEMES
====================================================

{scheme_text}

====================================================
FARMER QUESTION
====================================================

{question}

====================================================
YOUR TASK
====================================================

Answer like an experienced agricultural officer.

Always use:

1. Farmer profile

2. Disease prediction

3. Weather

4. Market prices

5. Yield prediction

6. Farm history

7. Government schemes

8. AI decisions

Prioritize:

Disease → Weather → Yield → Market → Schemes

Never recommend government schemes that are not listed.

====================================================
OUTPUT FORMAT
====================================================

🌾 Farm Summary

🦠 Disease Analysis

🌦 Weather Advisory

🧪 Fertilizer Recommendation

🌱 Yield Improvement

📈 Market Advice

🏛 Government Schemes

⚠ Risks

✅ Today's Action Plan

Use simple English suitable for Indian farmers.

"""

    return prompt