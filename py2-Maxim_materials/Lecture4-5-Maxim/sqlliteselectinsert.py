import sqlite3
conn = sqlite3.connect('hi2.db')
c = conn.cursor()
'''c.execute("""CREATE TABLE employees2 (
            first text,
            last text,
            pay integer
            )""")'''
c.execute("INSERT INTO employees2 VALUES (:first, :last, :pay)", {'first': "max", 'last': "iavich", 'pay': 100})
c.execute("INSERT INTO employees2 VALUES (:first, :last, :pay)", {'first': "maxi", 'last': "sanikidze", 'pay': 100})
c.execute("SELECT * FROM employees2 WHERE last='iavich'")
print (c.fetchall())
conn.commit()
conn.close()