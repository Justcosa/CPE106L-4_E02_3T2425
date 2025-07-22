import sqlite3

# Connect to the Chinook database
conn = sqlite3.connect('chinook.db')
cursor = conn.cursor()

# Query to select all rows from the employees table
cursor.execute("SELECT LastName, FirstName, Address FROM employees")

# Fetch all results
rows = cursor.fetchall()

# Print column names
column_names = [description[0] for description in cursor.description]
print('\t'.join(column_names))

# Print each row
for row in rows:
    print('\t'.join(str(item) for item in row))

# Close the connection
conn.close()
