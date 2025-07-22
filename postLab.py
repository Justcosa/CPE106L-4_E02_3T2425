import sqlite3

# Connect to the database
conn = sqlite3.connect('postLab.db')
cursor = conn.cursor()

# Example: Insert a new row into ADVENTURE_TRIP
# Replace the values with your actual column names and data
cursor.execute("""
    INSERT INTO ADVENTURE_TRIP (TRIP_ID, TRIP_NAME, START_LOCATION, STATE, DISTANCE, MAX_GRP_SIZE, TYPE, SEASON)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
""", (2, "Mapua Trip", "Home", "MNL", 25, 5, "Hiking", "Summer"))

conn.commit()  # Save (commit) the changes

# Query to select all rows from ADVENTURE_TRIP
cursor.execute("SELECT * FROM ADVENTURE_TRIP")

# Fetch and display the results
rows = cursor.fetchall()
for row in rows:
    print(row)

# Clean up
cursor.close()
conn.close()