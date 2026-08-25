import sqlite3
from pathlib import Path


# ============================================================
# DATABASE LOCATION
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASE_PATH = BASE_DIR / "database.db"


# ============================================================
# DATABASE CONNECTION
# ============================================================

def get_connection():

    conn = sqlite3.connect(
        DATABASE_PATH,
        check_same_thread=False
    )

    conn.row_factory = sqlite3.Row

    return conn


# ============================================================
# INITIALIZE DATABASE
# ============================================================

def init_database():

    conn = get_connection()

    cursor = conn.cursor()

    # ========================================================
    # FARMERS TABLE
    # ========================================================

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS farmers (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            farmer_id TEXT UNIQUE NOT NULL,

            farmer_name TEXT NOT NULL,

            mobile TEXT UNIQUE NOT NULL,

            password TEXT NOT NULL,

            state TEXT,

            district TEXT,

            village TEXT,

            crop TEXT,

            land_area REAL,

            soil_type TEXT,

            irrigation TEXT,

            farming_type TEXT,

            age INTEGER,

            gender TEXT,

            annual_income REAL,

            fpo_member TEXT,

            created_at
                TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )
        """
    )

    # ========================================================
    # PREDICTION HISTORY TABLE
    # ========================================================

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS prediction_history (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            farmer_id TEXT NOT NULL,

            crop TEXT,

            fertilizer TEXT,

            disease TEXT,

            disease_confidence REAL,

            yield_prediction REAL,

            production REAL,

            revenue REAL,

            weather TEXT,

            temperature REAL,

            humidity REAL,

            prediction_date
                TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )
        """
    )

    conn.commit()

    conn.close()


# ============================================================
# FARMER REGISTRATION
# ============================================================

def register_farmer(

    farmer_name,
    mobile,
    password,
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

    # --------------------------------------------------------
    # Check existing mobile
    # --------------------------------------------------------

    cursor.execute(
        """
        SELECT farmer_id

        FROM farmers

        WHERE mobile = ?

        LIMIT 1
        """,

        (mobile,)
    )

    existing = cursor.fetchone()

    if existing:

        conn.close()

        return None


    # --------------------------------------------------------
    # Generate Farmer ID
    # --------------------------------------------------------

    farmer_id = "F" + mobile


    try:

        cursor.execute(
            """
            INSERT INTO farmers (

                farmer_id,

                farmer_name,

                mobile,

                password,

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

            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,

            (

                farmer_id,

                farmer_name,

                mobile,

                password,

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
        )

        conn.commit()

        conn.close()

        return farmer_id

    except sqlite3.IntegrityError:

        conn.close()

        return None


# ============================================================
# FARMER LOGIN
# ============================================================

def authenticate_farmer(

    mobile,
    password

):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *

        FROM farmers

        WHERE mobile = ?

        AND password = ?

        LIMIT 1
        """,

        (

            mobile,

            password

        )
    )

    farmer = cursor.fetchone()

    conn.close()

    if farmer:

        return dict(farmer)

    return None


# ============================================================
# GET FARMER BY ID
# ============================================================

def get_farmer(

    farmer_id

):

    conn = get_connection()

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

    farmer = cursor.fetchone()

    conn.close()

    if farmer:

        return dict(farmer)

    return None


# ============================================================
# GET FARMER BY MOBILE
# ============================================================

def get_farmer_by_mobile(

    mobile

):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *

        FROM farmers

        WHERE mobile = ?

        LIMIT 1
        """,

        (mobile,)
    )

    farmer = cursor.fetchone()

    conn.close()

    if farmer:

        return dict(farmer)

    return None


# ============================================================
# UPDATE FARMER PROFILE
# ============================================================

def update_farmer_profile(

    farmer_id,

    farmer_name=None,
    state=None,
    district=None,
    village=None,
    crop=None,
    land_area=None,
    soil_type=None,
    irrigation=None,
    farming_type=None,
    age=None,
    gender=None,
    annual_income=None,
    fpo_member=None

):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE farmers

        SET

            farmer_name = COALESCE(?, farmer_name),

            state = COALESCE(?, state),

            district = COALESCE(?, district),

            village = COALESCE(?, village),

            crop = COALESCE(?, crop),

            land_area = COALESCE(?, land_area),

            soil_type = COALESCE(?, soil_type),

            irrigation = COALESCE(?, irrigation),

            farming_type = COALESCE(?, farming_type),

            age = COALESCE(?, age),

            gender = COALESCE(?, gender),

            annual_income = COALESCE(?, annual_income),

            fpo_member = COALESCE(?, fpo_member)

        WHERE farmer_id = ?
        """,

        (

            farmer_name,

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

            farmer_id

        )
    )

    conn.commit()

    conn.close()


# ============================================================
# INSERT COMPLETE PREDICTION
# ============================================================

def insert_prediction(

    farmer_id,

    crop=None,

    fertilizer=None,

    yield_prediction=None,

    production=None,

    revenue=None,

    disease=None,

    disease_confidence=None,

    weather=None,

    temperature=None,

    humidity=None

):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO prediction_history (

            farmer_id,

            crop,

            fertilizer,

            disease,

            disease_confidence,

            yield_prediction,

            production,

            revenue,

            weather,

            temperature,

            humidity

        )

        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,

        (

            farmer_id,

            crop,

            fertilizer,

            disease,

            disease_confidence,

            yield_prediction,

            production,

            revenue,

            weather,

            temperature,

            humidity

        )
    )

    conn.commit()

    prediction_id = cursor.lastrowid

    conn.close()

    return prediction_id


# ============================================================
# SAVE DISEASE
# ============================================================

def save_disease(

    farmer_id,

    disease,

    confidence

):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO prediction_history (

            farmer_id,

            disease,

            disease_confidence

        )

        VALUES (?, ?, ?)
        """,

        (

            farmer_id,

            disease,

            confidence

        )
    )

    conn.commit()

    prediction_id = cursor.lastrowid

    conn.close()

    return prediction_id


# ============================================================
# SAVE FERTILIZER
# ============================================================

def save_fertilizer(

    farmer_id,

    fertilizer

):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE prediction_history

        SET fertilizer = ?

        WHERE id = (

            SELECT id

            FROM prediction_history

            WHERE farmer_id = ?

            ORDER BY prediction_date DESC, id DESC

            LIMIT 1

        )
        """,

        (

            fertilizer,

            farmer_id

        )
    )

    conn.commit()

    conn.close()


# ============================================================
# SAVE YIELD
# ============================================================

def save_yield(

    farmer_id,

    yield_prediction,

    production,

    revenue

):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE prediction_history

        SET

            yield_prediction = ?,

            production = ?,

            revenue = ?

        WHERE id = (

            SELECT id

            FROM prediction_history

            WHERE farmer_id = ?

            ORDER BY prediction_date DESC, id DESC

            LIMIT 1

        )
        """,

        (

            yield_prediction,

            production,

            revenue,

            farmer_id

        )
    )

    conn.commit()

    conn.close()


# ============================================================
# SAVE WEATHER
# ============================================================

def save_weather(

    farmer_id,

    weather,

    temperature,

    humidity

):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE prediction_history

        SET

            weather = ?,

            temperature = ?,

            humidity = ?

        WHERE id = (

            SELECT id

            FROM prediction_history

            WHERE farmer_id = ?

            ORDER BY prediction_date DESC, id DESC

            LIMIT 1

        )
        """,

        (

            weather,

            temperature,

            humidity,

            farmer_id

        )
    )

    conn.commit()

    conn.close()


# ============================================================
# SAVE CROP
# ============================================================

def save_crop(

    farmer_id,

    crop

):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE prediction_history

        SET crop = ?

        WHERE id = (

            SELECT id

            FROM prediction_history

            WHERE farmer_id = ?

            ORDER BY prediction_date DESC, id DESC

            LIMIT 1

        )
        """,

        (

            crop,

            farmer_id

        )
    )

    conn.commit()

    conn.close()


# ============================================================
# LATEST PREDICTION
# ============================================================

def latest_prediction(

    farmer_id

):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *

        FROM prediction_history

        WHERE farmer_id = ?

        ORDER BY prediction_date DESC, id DESC

        LIMIT 1
        """,

        (farmer_id,)
    )

    data = cursor.fetchone()

    conn.close()

    if data:

        return dict(data)

    return None


# ============================================================
# ALL PREDICTIONS
# ============================================================

def get_prediction_history(

    farmer_id

):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *

        FROM prediction_history

        WHERE farmer_id = ?

        ORDER BY prediction_date DESC, id DESC
        """,

        (farmer_id,)
    )

    data = cursor.fetchall()

    conn.close()

    return [dict(row) for row in data]


# ============================================================
# DELETE FARMER HISTORY
# ============================================================

def clear_prediction_history(

    farmer_id

):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM prediction_history

        WHERE farmer_id = ?
        """,

        (farmer_id,)
    )

    conn.commit()

    conn.close()


# ============================================================
# INITIALIZE DATABASE
# ============================================================

init_database()