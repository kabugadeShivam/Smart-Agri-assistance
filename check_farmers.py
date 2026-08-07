import sqlite3

conn = sqlite3.connect("database/predictions.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM farmer_profile")

rows = cursor.fetchall()

print("Total Farmers:", len(rows))

for row in rows:
    print(row)

conn.close()