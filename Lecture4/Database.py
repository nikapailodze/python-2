# mongodb://localhost:27017

import pymongo

myclient=pymongo.MongoClient("mongodb://localhost:27017")
mydb=myclient["Caucasus_University"]
mycol=mydb["students"]



mydict={"name":"gio","address": "kavtaradze"}



x=mycol.insert_one(mydict)


mydict={"name":"sbaa","address": "vake"}
x=mycol.insert_one(mydict)

# for x in mycol.find():
#     print(x)

# myquery={"address": "vake"}
# mydoc=mycol.find(myquery)

# sort
# mydoc=mycol.find().sort("name")

# delete

myquery={"address":"kavtaradze"}
mycol.delete_many(myquery)

# drop
# mycol.drop()


# print("your query")

# for x in mydoc:
#     print(x)

# print("everyting form db")
# for i in mycol.find():
#     print(i)


# update

myquery={"address":"vake"}
newvalues={"$set": {"address": "Dighomi"}}

mycol.update_many(myquery,newvalues)

print("everyting form db")
for i in mycol.find():
    print(i)