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
    "1. Rodney Weaver'dan fazla maaş alanlar:",
    """
    SELECT first_name, last_name, salary
    FROM employees
    WHERE salary > (
        SELECT salary FROM employees
        WHERE first_name = 'Rodney' AND last_name = 'Weaver'
    );
    """
)

calistir(
    "2. Ortalama, en düşük ve en yüksek maaş:",
    """
    SELECT AVG(salary), MIN(salary), MAX(salary)
    FROM employees;
    """
)

calistir(
    "3. Maaşı 8700'den fazla olanlar:",
    """
    SELECT first_name, last_name, salary
    FROM employees
    WHERE salary > 8700;
    """
)

calistir(
    "4. Operations departmanında çalışanlar:",
    """
    SELECT e.first_name, e.last_name
    FROM employees e
    JOIN departments d ON e.emp_id = d.emp_id
    WHERE d.dept_name = 'Operations';
    """
)

calistir(
    "5. Technology departmanında çalışanlar:",
    """
    SELECT e.first_name, e.last_name
    FROM employees e
    JOIN departments d ON e.emp_id = d.emp_id
    WHERE d.dept_name = 'Technology';
    """
)

cur.close()
conn.close()