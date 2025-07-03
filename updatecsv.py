import psycopg2
import csv

#Db complete details
db_host = "localhost"
db_name = "mydb"
db_user = "postgres"
db_password = "1234"

csv_file_path = "userdata.csv"

#DB check with given credentials
try:
    conn = psycopg2.connect(
        host=db_host,
        database=db_name,
        user=db_user,
        password=db_password
    )
    conn.set_session(autocommit=True)
    cur = conn.cursor()

    # Ensure table exists
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        username VARCHAR(50) NOT NULL,
        email VARCHAR(100) NOT NULL
    )
    """)

    # Read CSV and update rows
    with open(csv_file_path, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            user_id = row['id']
            username = row['username']
            email = row['email']
            #below command will execute the update script for the database
            cur.execute("""
                UPDATE users
                SET username = %s, email = %s
                WHERE id = %s
            """, (username, email, user_id))

    print("Table updated successfully using CSV!")

    # Show updated data
    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()
    print("Current Data in Table:")
    for row in rows:
        print(row)
#closing command for script
except Exception as e:
    print("Error:", e)

finally:
    if conn:
        cur.close()
        conn.close()
