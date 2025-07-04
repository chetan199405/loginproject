import psycopg2
import csv

db_host = "localhost"
db_name = "mydb"
db_user = "postgres"
db_password = "1234"

csv_file_path = "userdata.csv"  # Make sure this file is in the same folder

try:
    conn = psycopg2.connect(
        host=db_host,
        database=db_name,
        user=db_user,
        password=db_password
    )
    conn.set_session(autocommit=True)
    cur = conn.cursor()

    # Create table if not exists
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        username VARCHAR(50) NOT NULL,
        email VARCHAR(100) NOT NULL
    )
    """)

    # Open and read the CSV file
    with open(csv_file_path, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        data = []
        for row in reader:
            data.append((row['username'], row['email']))

    # Insert multiple rows
    cur.executemany("INSERT INTO users (username, email) VALUES (%s, %s)", data)
    print(f"{len(data)} users added successfully from CSV!")

    # Show data in table
    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()
    print("Current Data in Table:")
    for row in rows:
        print(row)

except Exception as e:
    print("Error:", e)

finally:
    if conn:
        cur.close()
        conn.close()
