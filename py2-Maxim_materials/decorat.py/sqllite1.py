import sqlite3

import job

conn=sqlite3.connect(':memory:')

c=conn.cursor()

c.execute("""CREATE TABLE friends
          (name text,
            lastname text,
          age integer
          )""")


def insert_friend(fr):
    with conn:
        c.execute("INSERT INTO friends VALUES(:name,:lastname,:age)",
                  {"name":fr.name,"lastname":fr.surname,"age":fr.age})



def get_friend(name):
    c.execute("SELECT * FROM friends WHERE name=:name",{"name":name})
    return c.fetchall()

def update_age(fr,age):
    with conn:
        c.execute("""UPDATE friends SET age=:age
                  WHERE name=:name AND lastname=:lastname""",
                  {"name":fr.name,"lastname":fr.surname,"age":age})

def remove_fr(fr):
    with conn:
        c.execute("DELETE FROM friends WHERE name=:name AND lastname=:lastname",
                  {"name":fr.name,"lastname":fr.surname})

fr_1=job.fr_1
fr_2=job.fr_2

print(fr_1.fullname)
print(fr_2.fullname)


insert_friend(job.Friends("gia","suramela",100))
insert_friend(fr_1)
a=get_friend("gia")
b=get_friend("nuki")

update_age(fr_1,30)
remove_fr(fr_1)
a=get_friend("gia")
b=get_friend("nuki")

print(a,b)