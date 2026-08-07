from utils.farmer_memory import (
    save_memory,
    get_latest_memory
)

# ==========================================================
# Disease
# ==========================================================

def save_disease(
    farmer_id,
    disease,
    confidence
):

    latest = get_latest_memory(farmer_id)

    save_memory(

        farmer_id=farmer_id,

        crop=latest["crop"] if latest else None,
        soil=latest["soil"] if latest else None,

        fertilizer=latest["fertilizer"] if latest else None,

        disease=disease,
        confidence=confidence,

        yield_prediction=latest["yield_prediction"] if latest else None,
        production=latest["production"] if latest else None,
        revenue=latest["revenue"] if latest else None,

        weather=latest["weather"] if latest else None,

        market=latest["market"] if latest else None,

        government_scheme=latest["government_scheme"] if latest else None,

        farm_health=latest["farm_health"] if latest else None

    )


# ==========================================================
# Fertilizer
# ==========================================================

def save_fertilizer(

    farmer_id,

    fertilizer

):

    latest = get_latest_memory(farmer_id)

    save_memory(

        farmer_id=farmer_id,

        crop=latest["crop"] if latest else None,
        soil=latest["soil"] if latest else None,

        fertilizer=fertilizer,

        disease=latest["disease"] if latest else None,
        confidence=latest["confidence"] if latest else None,

        yield_prediction=latest["yield_prediction"] if latest else None,
        production=latest["production"] if latest else None,
        revenue=latest["revenue"] if latest else None,

        weather=latest["weather"] if latest else None,

        market=latest["market"] if latest else None,

        government_scheme=latest["government_scheme"] if latest else None,

        farm_health=latest["farm_health"] if latest else None

    )


# ==========================================================
# Yield
# ==========================================================

def save_yield(

    farmer_id,

    yield_prediction,

    production,

    revenue

):

    latest = get_latest_memory(farmer_id)

    save_memory(

        farmer_id=farmer_id,

        crop=latest["crop"] if latest else None,
        soil=latest["soil"] if latest else None,

        fertilizer=latest["fertilizer"] if latest else None,

        disease=latest["disease"] if latest else None,
        confidence=latest["confidence"] if latest else None,

        yield_prediction=yield_prediction,
        production=production,
        revenue=revenue,

        weather=latest["weather"] if latest else None,

        market=latest["market"] if latest else None,

        government_scheme=latest["government_scheme"] if latest else None,

        farm_health=latest["farm_health"] if latest else None

    )


# ==========================================================
# Weather
# ==========================================================

def save_weather(

    farmer_id,

    weather,

):

    latest = get_latest_memory(farmer_id)

    save_memory(

        farmer_id=farmer_id,

        crop=latest["crop"] if latest else None,
        soil=latest["soil"] if latest else None,

        fertilizer=latest["fertilizer"] if latest else None,

        disease=latest["disease"] if latest else None,
        confidence=latest["confidence"] if latest else None,

        yield_prediction=latest["yield_prediction"] if latest else None,
        production=latest["production"] if latest else None,
        revenue=latest["revenue"] if latest else None,

        weather=weather,

        market=latest["market"] if latest else None,

        government_scheme=latest["government_scheme"] if latest else None,

        farm_health=latest["farm_health"] if latest else None

    )


# ==========================================================
# Market
# ==========================================================

def save_market(

    farmer_id,

    market

):

    latest = get_latest_memory(farmer_id)

    save_memory(

        farmer_id=farmer_id,

        crop=latest["crop"] if latest else None,
        soil=latest["soil"] if latest else None,

        fertilizer=latest["fertilizer"] if latest else None,

        disease=latest["disease"] if latest else None,
        confidence=latest["confidence"] if latest else None,

        yield_prediction=latest["yield_prediction"] if latest else None,
        production=latest["production"] if latest else None,
        revenue=latest["revenue"] if latest else None,

        weather=latest["weather"] if latest else None,

        market=market,

        government_scheme=latest["government_scheme"] if latest else None,

        farm_health=latest["farm_health"] if latest else None

    )


# ==========================================================
# Latest Memory
# ==========================================================

def latest_prediction(

    farmer_id

):

    return get_latest_memory(farmer_id)