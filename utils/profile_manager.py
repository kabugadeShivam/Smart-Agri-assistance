from utils.database import get_connection


# ============================================================
# GET FARMER PROFILE
# ============================================================

def get_profile(farmer_id):
    """
    Fetch the complete farmer profile
    from the existing farmers table.
    """

    if not farmer_id:
        return {}

    conn = get_connection()

    try:
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM farmers
            WHERE farmer_id = ?
            LIMIT 1
            """,
            (farmer_id,)
        )

        row = cursor.fetchone()

        if row is None:
            return {}

        return dict(row)

    finally:
        conn.close()


# ============================================================
# SAVE / UPDATE FARMER PROFILE
# ============================================================

def update_profile(farmer_id, **fields):
    """
    Update selected farmer profile fields.

    Example:

        update_profile(
            farmer_id,
            crop="Rice",
            land_area=5
        )
    """

    if not farmer_id:
        return False

    if not fields:
        return False

    # Security: only allow actual farmer-profile columns.
    allowed_fields = {
        "farmer_name",
        "mobile",
        "state",
        "district",
        "village",
        "crop",
        "land_area",
        "soil_type",
        "irrigation",
        "farming_type",
        "age",
        "gender",
        "annual_income",
        "fpo_member",
    }

    clean_fields = {
        key: value
        for key, value in fields.items()
        if key in allowed_fields
    }

    if not clean_fields:
        return False

    conn = get_connection()

    try:
        cursor = conn.cursor()

        set_clause = ", ".join(
            f"{key} = ?"
            for key in clean_fields
        )

        values = list(clean_fields.values())
        values.append(farmer_id)

        query = f"""
            UPDATE farmers
            SET {set_clause}
            WHERE farmer_id = ?
        """

        cursor.execute(query, values)

        conn.commit()

        return cursor.rowcount > 0

    finally:
        conn.close()


# ============================================================
# REFRESH PROFILE
# ============================================================

def refresh_profile(farmer_id):
    """
    Fetch latest profile data from database.
    """

    return get_profile(farmer_id)


# ============================================================
# PROFILE EXISTS
# ============================================================

def profile_exists(farmer_id):
    """
    Check whether a farmer profile exists.
    """

    if not farmer_id:
        return False

    conn = get_connection()

    try:
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT 1
            FROM farmers
            WHERE farmer_id = ?
            LIMIT 1
            """,
            (farmer_id,)
        )

        return cursor.fetchone() is not None

    finally:
        conn.close()


# ============================================================
# GET PROFILE FIELD
# ============================================================

def get_profile_field(
    farmer_id,
    field,
    default=None
):
    """
    Get one specific field from farmer profile.
    """

    profile = get_profile(farmer_id)

    if not profile:
        return default

    return profile.get(
        field,
        default
    )


# ============================================================
# FARM PROFILE SUMMARY
# ============================================================

def profile_summary(farmer_id):
    """
    Return a clean summary useful for
    AI recommendations and Home page.
    """

    profile = get_profile(farmer_id)

    if not profile:
        return {}

    return {
        "farmer_id": profile.get("farmer_id"),
        "farmer_name": profile.get("farmer_name"),
        "mobile": profile.get("mobile"),

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

        "annual_income": profile.get(
            "annual_income"
        ),

        "fpo_member": profile.get(
            "fpo_member"
        ),
    }