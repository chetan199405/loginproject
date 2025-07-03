import psycopg2

db_host = "localhost"
db_name = "mydb"
db_user = "postgres"
db_password = "1234"

# Data to insert with default handling
username = input("Enter username (default: ram): ").strip()
if not username:
    username = "ram"

email = input("Enter email (default: ram@gmail.com): ").strip()
if not email:
    email = "ram@gmail.com"

try:
    conn = psycopg2.connect(
        host=db_host,
        database=db_name,
        user=db_user,
        password=db_password
    )
    conn.set_session(autocommit=True)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        username VARCHAR(50) NOT NULL,
        email VARCHAR(100) NOT NULL
    )
    """)

    cur.execute("INSERT INTO users (username, email) VALUES (%s, %s)", (username, email))
    print("User added successfully!")

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
