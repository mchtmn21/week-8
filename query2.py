import psycopg2

conn = psycopg2.connect(
    host="localhost",
    dbname="postgres",
    user="postgres",
    password="1234",
    port=5433
)

cur = conn.cursor()


def calistir(baslik, sorgu):
    cur.execute(sorgu)
    satirlar = cur.fetchall()
    print("\n" + baslik)
    for satir in satirlar:
        print(satir)


calistir(
    "6. Kadın çalışanların ortalama maaşı:",
    """
    SELECT AVG(salary)
    FROM employees
    WHERE gender = 'Female';
    """
)

calistir(
    "7. Her departmanın ortalama maaşı:",
    """
    SELECT d.dept_name, AVG(e.salary)
    FROM employees e
    JOIN departments d ON e.emp_id = d.emp_id
    GROUP BY d.dept_name;
    """
)

calistir(
    "8. En eski ve en yeni işe alınan çalışanlar:",
    """
    SELECT first_name, last_name, hire_date
    FROM employees
    WHERE hire_date = (SELECT MIN(hire_date) FROM employees)
       OR hire_date = (SELECT MAX(hire_date) FROM employees);
    """
)

calistir(
    "9. En yüksek maaşlı çalışanın işe alınma tarihi ve departmanı:",
    """
    SELECT e.hire_date, d.dept_name
    FROM employees e
    LEFT JOIN departments d ON e.emp_id = d.emp_id
    WHERE e.salary = (SELECT MAX(salary) FROM employees);
    """
)

calistir(
    "10. En düşük maaşlı çalışanın işe alınma tarihi ve departmanı:",
    """
    SELECT e.hire_date, d.dept_name
    FROM employees e
    LEFT JOIN departments d ON e.emp_id = d.emp_id
    WHERE e.salary = (SELECT MIN(salary) FROM employees);
    """
)

cur.close()
conn.close()