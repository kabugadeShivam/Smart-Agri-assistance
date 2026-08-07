from .context_builder import build_context


# =====================================================
# AI Decision Engine
# =====================================================

def generate_decisions():

    ctx = build_context()

    decisions = []

    # =====================================================
    # Disease Analysis
    # =====================================================

    disease = ctx.get("disease")

    if disease and str(disease).lower() != "healthy":

        decisions.append({

            "priority": "Critical",

            "title": "Disease Alert",

            "action": f"Treat {disease} immediately.",

            "reason": "Disease detected by AI model."

        })

    # =====================================================
    # Fertilizer
    # =====================================================

    fertilizer = ctx.get("fertilizer")

    if fertilizer:

        decisions.append({

            "priority": "High",

            "title": "Fertilizer Recommendation",

            "action": f"Apply {fertilizer}.",

            "reason": "Based on soil nutrient analysis."

        })

    # =====================================================
    # Yield Prediction
    # =====================================================

    predicted_yield = ctx.get("yield")

    if predicted_yield is not None:

        try:

            if float(predicted_yield) < 4:

                decisions.append({

                    "priority": "High",

                    "title": "Low Yield Risk",

                    "action": "Improve irrigation and nutrient management.",

                    "reason": f"Predicted yield is only {predicted_yield}."

                })

            else:

                decisions.append({

                    "priority": "Low",

                    "title": "Yield Status",

                    "action": f"Expected yield: {predicted_yield}",

                    "reason": "Yield prediction is satisfactory."

                })

        except Exception:

            pass

    # =====================================================
    # Weather
    # =====================================================

    weather = ctx.get("weather")

    if isinstance(weather, dict):

        rainfall = weather.get("rainfall", 0)

        temperature = weather.get("temperature", 0)

        if rainfall > 10:

            decisions.append({

                "priority": "High",

                "title": "Heavy Rain Warning",

                "action": "Avoid fertilizer or pesticide spraying today.",

                "reason": "Heavy rainfall is forecast."

            })

        if temperature > 35:

            decisions.append({

                "priority": "Medium",

                "title": "High Temperature",

                "action": "Irrigate during early morning or evening.",

                "reason": "Extreme heat can stress crops."

            })

    # =====================================================
    # Market
    # =====================================================

    market = ctx.get("market")

    if isinstance(market, dict):

        trend = market.get("trend")

        if trend == "Rising":

            decisions.append({

                "priority": "Medium",

                "title": "Market Opportunity",

                "action": "Delay selling for a better price.",

                "reason": "Market trend is rising."

            })

        elif trend == "Falling":

            decisions.append({

                "priority": "Medium",

                "title": "Market Alert",

                "action": "Consider selling soon.",

                "reason": "Market prices are falling."

            })

    # =====================================================
    # Farm Health
    # =====================================================

    health = ctx.get("farm_health")

    if health is not None:

        try:

            if health < 50:

                decisions.append({

                    "priority": "Critical",

                    "title": "Poor Farm Health",

                    "action": "Immediate farm inspection required.",

                    "reason": f"Farm health score is {health}."

                })

            elif health < 75:

                decisions.append({

                    "priority": "Medium",

                    "title": "Farm Health",

                    "action": "Improve crop management practices.",

                    "reason": f"Farm health score is {health}."

                })

        except Exception:

            pass

    # =====================================================
    # Government Schemes
    # =====================================================

    schemes = ctx.get("schemes")

    if schemes:

        decisions.append({

            "priority": "Low",

            "title": "Government Schemes",

            "action": f"You are eligible for {len(schemes)} schemes.",

            "reason": "AI matched schemes based on your profile."

        })

    # =====================================================
    # Priority Sorting
    # =====================================================

    priority_order = {

        "Critical": 1,

        "High": 2,

        "Medium": 3,

        "Low": 4

    }

    decisions = sorted(

        decisions,

        key=lambda x: priority_order.get(

            x["priority"],

            5

        )

    )

    return decisions