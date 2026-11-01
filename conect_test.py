import psycopg2

conn = psycopg2.connect(
    host="localhost",
    dbname="postgres",
    user="postgres",
    password="1234",
    port=5433
)

cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        emp_id INT PRIMARY KEY,
        first_name VARCHAR(50),
        last_name VARCHAR(50),
        salary INT,
        job_title VARCHAR(100),
        gender VARCHAR(10),
        hire_date DATE
    );
""")

conn.commit()
print("employees tablosu hazir.")

cur.close()
conn.close()