from utils.farmer_memory import get_history


# =====================================================
# Build AI History Context
# =====================================================

def build_history_context(farmer_id):

    history = get_history(farmer_id)

    if not history:
        return "No previous farming history available."

    context = []

    context.append("===== PREVIOUS FARM HISTORY =====\n")

    # Last 10 records
    for item in history[-10:]:

        record = f"""
Date: {item.get('created_at', 'N/A')}

Crop: {item.get('crop', 'N/A')}

Disease: {item.get('disease', 'Healthy')}

Confidence: {item.get('confidence', 'N/A')}

Fertilizer: {item.get('fertilizer', 'N/A')}

Yield Prediction: {item.get('yield_prediction', 'N/A')}

Production: {item.get('production', 'N/A')}

Revenue: {item.get('revenue', 'N/A')}

Weather: {item.get('weather', 'N/A')}

Market: {item.get('market', 'N/A')}

Government Scheme: {item.get('government_scheme', 'N/A')}

Farm Health: {item.get('farm_health', 'N/A')}

------------------------------------------
"""

        context.append(record)

    return "\n".join(context)