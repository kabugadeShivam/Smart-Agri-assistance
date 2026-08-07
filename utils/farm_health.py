def calculate_farm_health(

    disease,

    confidence,

    yield_prediction,

    rainfall,

    temperature,

    moisture

):

    score = 100

    advice = []

    # ----------------------------
    # Disease
    # ----------------------------

    if disease.lower() != "healthy":

        score -= 25

        advice.append(
            "Disease detected. Start treatment immediately."
        )

    # ----------------------------
    # Confidence
    # ----------------------------

    if confidence > 90:

        score -= 5

    # ----------------------------
    # Yield
    # ----------------------------

    if yield_prediction < 2:

        score -= 20

        advice.append(
            "Very low expected yield."
        )

    elif yield_prediction < 4:

        score -= 10

    # ----------------------------
    # Rainfall
    # ----------------------------

    if rainfall < 500:

        score -= 10

        advice.append(
            "Low rainfall. Irrigation recommended."
        )

    elif rainfall > 1500:

        score -= 8

        advice.append(
            "Heavy rainfall may increase disease risk."
        )

    # ----------------------------
    # Temperature
    # ----------------------------

    if temperature > 38:

        score -= 8

        advice.append(
            "High temperature stress."
        )

    # ----------------------------
    # Moisture
    # ----------------------------

    if moisture < 30:

        score -= 8

        advice.append(
            "Low soil moisture."
        )

    score = max(score, 0)

    if score >= 90:

        status = "Excellent"

    elif score >= 75:

        status = "Good"

    elif score >= 60:

        status = "Average"

    elif score >= 40:

        status = "Poor"

    else:

        status = "Critical"

    return score, status, advice