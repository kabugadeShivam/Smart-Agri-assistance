from utils.session_manager import get_all_predictions
from utils.auth import current_profile
from utils.scheme_matcher import match_schemes


# =====================================================
# Build Complete AI Context
# =====================================================

def build_context():

    profile = current_profile()

    memory = get_all_predictions()

    context = {}

    # =====================================================
    # Farmer Profile
    # =====================================================

    context["farmer"] = {

        "id": profile.get("farmer_id"),

        "name": profile.get("farmer_name"),

        "state": profile.get("state"),

        "district": profile.get("district"),

        "village": profile.get("village"),

        "crop": profile.get("crop"),

        "land_area": profile.get("land_area"),

        "soil_type": profile.get("soil_type"),

        "irrigation": profile.get("irrigation"),

        "farming_type": profile.get("farming_type"),

        "age": profile.get("age"),

        "gender": profile.get("gender"),

        "annual_income": profile.get("annual_income"),

        "fpo_member": profile.get("fpo_member")

    }

    # =====================================================
    # AI Prediction Memory
    # =====================================================

    context["disease"] = memory.get("disease")

    context["confidence"] = memory.get("confidence")

    context["fertilizer"] = memory.get("fertilizer")

    context["yield"] = memory.get("yield")

    context["production"] = memory.get("production")

    context["revenue"] = memory.get("revenue")

    context["weather"] = memory.get("weather")

    context["market"] = memory.get("market")

    context["farm_health"] = memory.get("farm_health")

    # =====================================================
    # Government Schemes
    # =====================================================

    schemes = match_schemes(

        state=profile.get("state"),

        district=profile.get("district"),

        crop=profile.get("crop"),

        land_area=profile.get("land_area"),

        age=profile.get("age"),

        gender=profile.get("gender")

    )

    context["schemes"] = schemes[:5]

    return context