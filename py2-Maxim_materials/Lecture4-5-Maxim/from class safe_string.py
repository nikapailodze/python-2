import sqlite3
import employer
conn = sqlite3.connect(':memory:')
c = conn.cursor()
c.execute("""CREATE TABLE employees (
            first text,
            last text,
            pay integer
            )""")
emp_1 = employer.Employee('John', 'Doe', 80000)
emp_2 = employer.Employee('Jane', 'Doe', 90000)
c.execute("INSERT INTO employees VALUES (?,?,?)",(emp_1.first, emp_1.last, emp_1.pay))
c.execute("INSERT INTO employees VALUES (?,?,?)",(emp_2.first, emp_2.last, emp_1.pay))
c.execute("SELECT * FROM employees WHERE last=?",('Doe',))
print (c.fetchall())
conn.commit()
conn.close()