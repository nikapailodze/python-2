import pymongo

myClient=pymongo.MongoClient("mongodb://localhost:27017")

mydb=myClient["Hello_Database"]

mycol=mydb["Hi-Hello"]


# mydict={"name":"nikolozi","surname":"pailodze","age":18}

# mycol.insert_one(mydict)

# for i in range(5):
#     name=input("write your name")
#     surname=input("write yoru surname")
#     age=input("write your age")
#     mydict={"name":name,"surname":surname,"age":age}
#     mycol.insert_one(mydict)


# for i in mycol.find():
#     newvalue={"$set":{"Job":input("what is your job")}}
#     mycol.update_one(i,newvalue)
#     # print(i["name"])
   

mydoc=mycol.find().sort("name")