from .decision_engine import generate_decisions


# =====================================================
# Daily Action Plan
# =====================================================

def get_daily_plan():

    decisions = generate_decisions()

    if not decisions:
        return "✅ No critical actions required today."

    priority_order = {
        "Critical": 1,
        "High": 2,
        "Medium": 3,
        "Low": 4
    }

    decisions = sorted(
        decisions,
        key=lambda x: priority_order.get(
            x.get("priority", "Medium"),
            3
        )
    )

    plan = []

    plan.append("🌾 DAILY FARM ACTION PLAN\n")

    for i, decision in enumerate(decisions, start=1):

        priority = decision.get("priority", "Medium")
        action = decision.get("action", "")
        reason = decision.get("reason", "")

        if priority == "Critical":
            icon = "🔴"

        elif priority == "High":
            icon = "🟠"

        elif priority == "Medium":
            icon = "🟡"

        else:
            icon = "🟢"

        plan.append(
            f"""{i}. {icon} {action}

Reason : {reason}

Priority : {priority}
"""
        )

    return "\n".join(plan)


# =====================================================
# Short Summary
# =====================================================

def get_summary():

    decisions = generate_decisions()

    if not decisions:
        return "Farm status is stable."

    return f"{len(decisions)} important recommendations generated today."