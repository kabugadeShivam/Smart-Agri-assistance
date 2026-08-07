from utils.database import get_connection


# =====================================================
# Register Farmer
# =====================================================

def register_farmer(
    name,
    mobile,
    state="",
    district="",
    village="",
    crop="",
    land_area=0,
    soil_type="",
    irrigation="",
    farming_type="",
    age=0,
    gender="",
    annual_income=0,
    fpo_member="No"
):

    conn = get_connection()
    cursor = conn.cursor()

    # Prevent duplicate mobile numbers
    cursor.execute(
        "SELECT farmer_id FROM farmer_profile WHERE mobile=?",
        (mobile,)
    )

    existing = cursor.fetchone()

    if existing:
        conn.close()
        raise Exception("Mobile number already registered.")

    cursor.execute(
        """
        INSERT INTO farmer_profile(

            farmer_name,
            mobile,
            state,
            district,
            village,
            crop,
            land_area,
            soil_type,
            irrigation,
            farming_type,
            age,
            gender,
            annual_income,
            fpo_member

        )

        VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)
        """,
        (
            name,
            mobile,
            state,
            district,
            village,
            crop,
            land_area,
            soil_type,
            irrigation,
            farming_type,
            age,
            gender,
            annual_income,
            fpo_member,
        ),
    )

    conn.commit()

    farmer_id = cursor.lastrowid

    conn.close()

    return farmer_id


# =====================================================
# Login
# =====================================================

def login(mobile):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM farmer_profile
        WHERE mobile=?
        """,
        (mobile,),
    )

    farmer = cursor.fetchone()

    conn.close()

    return farmer


# =====================================================
# Get Farmer Profile
# =====================================================

def get_profile(farmer_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM farmer_profile
        WHERE farmer_id=?
        """,
        (farmer_id,),
    )

    profile = cursor.fetchone()

    conn.close()

    return profile


# =====================================================
# Update Farmer Profile
# =====================================================

def update_profile(
    farmer_id,
    state,
    district,
    village,
    crop,
    land_area,
    soil_type,
    irrigation,
    farming_type,
    age,
    gender,
    annual_income,
    fpo_member,
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE farmer_profile

        SET

            state=?,
            district=?,
            village=?,
            crop=?,
            land_area=?,
            soil_type=?,
            irrigation=?,
            farming_type=?,
            age=?,
            gender=?,
            annual_income=?,
            fpo_member=?

        WHERE farmer_id=?
        """,
        (
            state,
            district,
            village,
            crop,
            land_area,
            soil_type,
            irrigation,
            farming_type,
            age,
            gender,
            annual_income,
            fpo_member,
            farmer_id,
        ),
    )

    conn.commit()
    conn.close()


# =====================================================
# Get Farmer By Mobile
# =====================================================

def get_farmer_by_mobile(mobile):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM farmer_profile
        WHERE mobile=?
        """,
        (mobile,),
    )

    farmer = cursor.fetchone()

    conn.close()

    return farmer


# =====================================================
# Get All Farmers (Admin/Future Use)
# =====================================================

def get_all_farmers():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM farmer_profile
        ORDER BY farmer_id DESC
        """
    )

    farmers = cursor.fetchall()

    conn.close()

    return farmers


# =====================================================
# Delete Farmer
# =====================================================

def delete_farmer(farmer_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM farmer_profile
        WHERE farmer_id=?
        """,
        (farmer_id,),
    )

    conn.commit()
    conn.close()