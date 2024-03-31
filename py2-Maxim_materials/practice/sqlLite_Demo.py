import sqlite3
from sqlLite import Employee


# on memery it starts fresh on every time
conn = sqlite3.connect(':memory:')

# cursor allows us to excecute some sql commands
c=conn.cursor()

c.execute("""CREATE TABLE employees (
            first text,
            last text,
            pay integer
            )""")


c.execute("INSERT INTO employees VALUES ('Nikolozi', 'Pailodze', 50000 )")
c.execute("INSERT INTO employees VALUES ('Mari', 'Pailodze', 70000 )")

# conn.commit()

emp_1= Employee("John","Doe",80000)
emp_2= Employee("Jane","Doe",90000)

print(emp_1.first)

# tupe instead of format to protect it
c.execute("INSERT INTO employees VALUES (?,?,?)", (emp_1.first,emp_1.last,emp_1.pay))

# or dictionrat key value
c.execute("INSERT INTO employees VALUES (:first, :last ,:pay)", {'first':emp_2.first,'last':emp_2.last,'pay':emp_2.pay,})

# Select statement
c.execute("SELECT * FROM employees WHERE last=?", ('Pailodze',))

print(c.fetchall())


c.execute("SELECT * FROM employees WHERE last=:last", {'last':"Doe"})

print(c.fetchall())
# it will get remaining rows that are left
# print(c.fetchall())

# This will get the next row and our result
# print(c.fetchone())

# this will return that number of rows as a list
# c.fetchmany(5)


def update_pay(emp,pay):
    with conn:
        c.execute("""UPDATE employees SET pay = :pay
                    WHERE first = :first AND last =:last""",
                    {'first':emp.first,'last':emp.last,'pay':emp.pay})

update_pay(emp_2,95500)

c.execute("SELECT * FROM employees WHERE last=:last", {'last':"Doe"})

print(c.fetchall())

# this commits current transaction 
conn.commit()

conn.close()