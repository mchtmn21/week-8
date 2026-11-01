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
    CREATE TABLE IF NOT EXISTS departments (
        emp_id INT PRIMARY KEY,
        dept_name VARCHAR(50),
        dept_id INT
    );
""")

cur.execute("""
    INSERT INTO departments (emp_id, dept_name, dept_id)
    VALUES
        (17679, 'Operations', 13),
        (26650, 'Marketing', 14),
        (30840, 'Operations', 13),
        (49823, 'Technology', 12),
        (51821, 'Operations', 13),
        (67323, 'Marketing', 14),
        (71119, 'Administrative', 11),
        (76589, 'Operations', 13),
        (97927, 'Technology', 12)
    ON CONFLICT (emp_id) DO NOTHING;
""")

conn.commit()
print("departments tablosu hazır ve veriler eklendi.")

cur.close()
conn.close()