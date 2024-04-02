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
emp_2 = employer.Employee('Jane', 'Doer', 90000)
c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first': emp_1.first, 'last': emp_1.last, 'pay': emp_1.pay})
c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first': emp_2.first, 'last': emp_2.last, 'pay': emp_2.pay})
c.execute("SELECT * FROM employees WHERE last=:last",{'last':"Doe"})
print (c.fetchall())
c.execute("SELECT * FROM employees WHERE pay>=90000")
print (c.fetchall())
conn.commit()
conn.close()