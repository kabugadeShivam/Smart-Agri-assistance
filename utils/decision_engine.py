def generate_recommendation(

    fertilizer,
    disease,
    confidence,
    temperature,
    humidity,
    rainfall,
    yield_prediction

):

    recommendations = []

    # -----------------------------
    # Weather
    # -----------------------------

    if rainfall > 100:

        recommendations.append(
            "🌧 Heavy rainfall expected. Delay fertilizer application."
        )

    elif rainfall < 30:

        recommendations.append(
            "💧 Rainfall is low. Irrigation is recommended."
        )

    # -----------------------------
    # Disease
    # -----------------------------

    if "healthy" not in disease.lower():

        recommendations.append(

            f"🦠 Disease detected: {disease.replace('_',' ')}"

        )

        recommendations.append(

            "Apply treatment immediately."

        )

    else:

        recommendations.append(

            "✅ Crop health looks good."

        )

    # -----------------------------
    # Confidence
    # -----------------------------

    if confidence > 95:

        recommendations.append(

            "AI prediction confidence is very high."

        )

    elif confidence < 70:

        recommendations.append(

            "Please verify prediction manually."

        )

    # -----------------------------
    # Fertilizer
    # -----------------------------

    recommendations.append(

        f"Recommended Fertilizer: {fertilizer}"

    )

    # -----------------------------
    # Yield
    # -----------------------------

    if yield_prediction > 5:

        recommendations.append(

            "Excellent expected yield."

        )

    else:

        recommendations.append(

            "Yield can be improved with better nutrient management."

        )

    return recommendations