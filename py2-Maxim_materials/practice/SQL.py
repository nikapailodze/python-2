import sqlite3

from sqlLite import Employee

conn=sqlite3.connect(':memory:')

c=conn.cursor()

c.execute("""CREATE TABLE monebi
          (first text,
           last text,
           pay integer)""" )

def insert_name(emp):
    with conn:
        c.execute("INSERT INTO monebi VALUES (:first,:last,:pay)", {"first":emp.first,"last":emp.last,"pay":emp.pay})

def get_emp(lastname):
    c.execute("SELECT * FROM monebi WHERE last=:last ", {"last": lastname} )
    return  c.fetchall()

def update_payment(emp,pay):
    with conn:
        c.execute("""UPDATE monebi SET pay=:pay WHERE first=:first AND last=:last """, 
                  {"first":emp.first,"last":emp.last,"pay":pay})
        


def remove_emp(emp):
    with conn:
        c.execute("DELETE FROM monebi WHERE  first=:first AND last=:last " ,{"first":emp.first,"last":emp.last})

emp_1=Employee("Niko","Laus",9090)
emp_2=Employee("Ubnis","Bichi",1000)

insert_name(emp_1)
insert_name(emp_2) 
a=get_emp("Laus")
b=get_emp("Bichi")
print(a,b)

remove_emp(emp_1)
update_payment(emp_2,95000)

a=get_emp("Laus")
b=get_emp("Bichi")

print(a,b)




conn.close()