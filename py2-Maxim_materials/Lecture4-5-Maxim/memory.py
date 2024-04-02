import sqlite3
conn = sqlite3.connect(':memory:')
c = conn.cursor()
c.execute("""CREATE TABLE employees (
            first text,
            last text,
            pay integer
            )""")
c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first': "max", 'last': "iavich", 'pay': 100})
c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first': "maxi", 'last': "iavich", 'pay': 100})
c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first': "kakha", 'last': "dobo", 'pay': 200})
c.execute("SELECT * FROM employees")
print (c.fetchall())
conn.commit()
conn.close()