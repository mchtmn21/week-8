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
    INSERT INTO employees (emp_id, first_name, last_name, salary, job_title, gender, hire_date)
    VALUES
        (17679, 'Robert', 'Gilmore', 110000, 'Operations Director', 'Male', '2018-09-04'),
        (26650, 'Elvis', 'Ritter', 86000, 'Sales Manager', 'Male', '2017-11-24'),
        (30840, 'David', 'Barrow', 85000, 'Data Scientist', 'Male', '2019-12-02'),
        (49714, 'Hugo', 'Forester', 55000, 'IT Support Specialist', 'Male', '2019-11-22'),
        (51821, 'Linda', 'Foster', 95000, 'Data Scientist', 'Female', '2019-04-29'),
        (67323, 'Lisa', 'Wiener', 75000, 'Business Analyst', 'Female', '2018-08-09'),
        (70950, 'Rodney', 'Weaver', 87000, 'Project Manager', 'Male', '2018-12-20'),
        (71329, 'Gayle', 'Meyer', 77000, 'HR Manager', 'Female', '2019-06-28'),
        (76589, 'Jason', 'Christian', 99000, 'Project Manager', 'Male', '2019-01-21'),
        (97927, 'Billie', 'Lanning', 67000, 'Web Developer', 'Female', '2018-06-25')
    ON CONFLICT (emp_id) DO NOTHING;
""")

conn.commit()
print("employees verileri eklendi.")

cur.close()
conn.close()