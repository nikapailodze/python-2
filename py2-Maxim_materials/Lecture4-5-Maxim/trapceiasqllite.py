import sqlite3
import trapezoidclass
conn = sqlite3.connect(':memory:')
c = conn.cursor()
c.execute("""CREATE TABLE Quadrilaterals (
            Trapezoid integer,
            Rectangle integer,
            Square integer
            )""")
tr1=trapezoidclass.Trapecia([5,7,12])
tr2=trapezoidclass.Trapecia([50,10,7])
m1=trapezoidclass.Martkutxedi([9,12,10])
m2=trapezoidclass.Martkutxedi([123,67,1])
sq1=trapezoidclass.Kvadrati([6,123,3])
sq2=trapezoidclass.Kvadrati([4,5,6])
c.execute("INSERT INTO Quadrilaterals VALUES (:Trapezoid, :Rectangle, :Square)", {'Trapezoid': tr1.fartobi(), 'Rectangle': m1.fartobi(), 'Square': sq1.fartobi()})
c.execute("INSERT INTO Quadrilaterals VALUES (:Trapezoid, :Rectangle, :Square)", {'Trapezoid': tr2.fartobi(), 'Rectangle': m2.fartobi(), 'Square': sq2.fartobi()})
c.execute("SELECT * FROM Quadrilaterals" )
print (c.fetchall())
c.execute("SELECT * FROM Quadrilaterals")
print (c.fetchall())
conn.commit()
conn.close()