import sqlite3
import trapezoid
conn=sqlite3.connect(":memory:")

c=conn.cursor()

c.execute("""CREATE  TABLE shapes
          (Trapezoid integer)
""")

def insert(trap):
    with conn:
        c.execute("INSERT INTO shapes VALUES(:Trapezoid)",
                  {"Trapezoid":trap.area()})


trap_1=trapezoid.Trapezoid([1,2,3])
trian_1=trapezoid.Triangle([5,7,8])
trian_2=trapezoid.Triangle([5,7,8])

insert(trap_1)
insert(trian_1)
insert(trian_2)
c.execute("SELECT * FROM shapes")
print(c.fetchall())

# print(trap_1.area())
# print(trap_2)
c.close()
