import sqlite3
from pathlib import Path

DATABASE = Path(__file__).parent.parent / "database" / "predictions.db"


def save_farmer(
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
):

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
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
    VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)
    """, (
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
    ))

    conn.commit()
    conn.close()


def get_farmer(mobile):

    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM farmer_profile WHERE mobile=?",
        (mobile,)
    )

    farmer = cursor.fetchone()

    conn.close()

    if farmer:
        return dict(farmer)

    return None


def update_farmer(
    mobile,
    crop,
    land_area,
    soil_type,
    irrigation
):

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("""
    UPDATE farmer_profile
    SET crop=?,
        land_area=?,
        soil_type=?,
        irrigation=?
    WHERE mobile=?
    """, (
        crop,
        land_area,
        soil_type,
        irrigation,
        mobile
    ))

    conn.commit()
    conn.close()


def delete_farmer(mobile):

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM farmer_profile WHERE mobile=?",
        (mobile,)
    )

    conn.commit()
    conn.close()