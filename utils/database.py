import sqlite3
from pathlib import Path

# =====================================================
# Database Path
# =====================================================

DATABASE = Path(__file__).parent.parent / "database" / "predictions.db"

print("Database Path:", DATABASE.resolve())


# =====================================================
# Database Connection
# =====================================================

def get_connection():
    """
    Returns SQLite connection with Row Factory enabled.
    """
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


# =====================================================
# Initialize Database
# =====================================================

def create_database():

    conn = get_connection()
    cursor = conn.cursor()

    # =====================================================
    # Farmer Profile (Master Table)
    # =====================================================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS farmer_profile(

        farmer_id INTEGER PRIMARY KEY AUTOINCREMENT,

        farmer_name TEXT NOT NULL,

        mobile TEXT UNIQUE NOT NULL,

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

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

    )
    """)

    # =====================================================
    # Prediction History
    # =====================================================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS prediction_history(

        prediction_id INTEGER PRIMARY KEY AUTOINCREMENT,

        farmer_id INTEGER,

        prediction_type TEXT,

        prediction TEXT,

        confidence REAL,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

        FOREIGN KEY(farmer_id)
        REFERENCES farmer_profile(farmer_id)

    )
    """)

    # =====================================================
    # AI Chat History
    # =====================================================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS chat_history(

        chat_id INTEGER PRIMARY KEY AUTOINCREMENT,

        farmer_id INTEGER,

        question TEXT,

        answer TEXT,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

        FOREIGN KEY(farmer_id)
        REFERENCES farmer_profile(farmer_id)

    )
    """)

    # =====================================================
    # Government Scheme History
    # =====================================================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS scheme_history(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        farmer_id INTEGER,

        scheme_name TEXT,

        benefit TEXT,

        matched_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

        FOREIGN KEY(farmer_id)
        REFERENCES farmer_profile(farmer_id)

    )
    """)

    # =====================================================
    # Market Recommendation History
    # =====================================================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS market_history(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        farmer_id INTEGER,

        crop TEXT,

        market TEXT,

        price REAL,

        trend TEXT,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

        FOREIGN KEY(farmer_id)
        REFERENCES farmer_profile(farmer_id)

    )
    """)

    conn.commit()
    conn.close()

    print("✅ Database Initialized Successfully")


# =====================================================
# Run Directly
# =====================================================

if __name__ == "__main__":
    create_database()