import sqlite3
import json
from pathlib import Path

# =====================================================
# Database
# =====================================================

DATABASE = Path(__file__).parent.parent / "database" / "predictions.db"


# =====================================================
# Connection
# =====================================================

def get_connection():

    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row

    return conn


# =====================================================
# Create Table
# =====================================================

def create_memory_table():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""

    CREATE TABLE IF NOT EXISTS farmer_memory(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        farmer_id INTEGER,

        crop TEXT,

        soil TEXT,

        fertilizer TEXT,

        disease TEXT,

        confidence REAL,

        yield_prediction REAL,

        production REAL,

        revenue REAL,

        weather TEXT,

        market TEXT,

        government_scheme TEXT,

        farm_health INTEGER,

        question TEXT,

        ai_response TEXT,

        recommendation TEXT,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

    )

    """)

    conn.commit()
    conn.close()


# =====================================================
# Save Memory
# =====================================================

def save_memory(

    farmer_id,

    crop=None,

    soil=None,

    fertilizer=None,

    disease=None,

    confidence=None,

    yield_prediction=None,

    production=None,

    revenue=None,

    weather=None,

    market=None,

    government_scheme=None,

    farm_health=None,

    question=None,

    ai_response=None,

    recommendation=None

):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""

    INSERT INTO farmer_memory(

        farmer_id,

        crop,

        soil,

        fertilizer,

        disease,

        confidence,

        yield_prediction,

        production,

        revenue,

        weather,

        market,

        government_scheme,

        farm_health,

        question,

        ai_response,

        recommendation

    )

    VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)

    """,(

        farmer_id,

        crop,

        soil,

        fertilizer,

        disease,

        confidence,

        yield_prediction,

        production,

        revenue,

        json.dumps(weather) if weather else None,

        json.dumps(market) if market else None,

        government_scheme,

        farm_health,

        question,

        ai_response,

        recommendation

    ))

    conn.commit()

    conn.close()


# =====================================================
# History
# =====================================================

def get_history(farmer_id):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""

    SELECT *

    FROM farmer_memory

    WHERE farmer_id=?

    ORDER BY created_at DESC

    """,(farmer_id,))

    rows = cursor.fetchall()

    conn.close()

    history=[]

    for row in rows:

        record=dict(row)

        if record["weather"]:

            try:
                record["weather"]=json.loads(record["weather"])
            except:
                pass

        if record["market"]:

            try:
                record["market"]=json.loads(record["market"])
            except:
                pass

        history.append(record)

    return history


# =====================================================
# Latest Memory
# =====================================================

def get_latest_memory(farmer_id):

    history=get_history(farmer_id)

    if not history:

        return None

    return history[0]


# =====================================================
# Delete Farmer Memory
# =====================================================

def clear_memory(farmer_id):

    conn=get_connection()

    cursor=conn.cursor()

    cursor.execute("""

    DELETE FROM farmer_memory

    WHERE farmer_id=?

    """,(farmer_id,))

    conn.commit()

    conn.close()


# =====================================================
# Create Table Automatically
# =====================================================

create_memory_table()