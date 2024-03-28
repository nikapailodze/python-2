import random
import pymongo

myclient=pymongo.MongoClient("mongodb://localhost:27017")
mydb= myclient["Caucasus_University"]

mycol=mydb["students"]

myDict=dict()

for i in range(0,10):
   
    myDict[str(random.randrange(0,100))]=random.randrange(0,100)

x=mycol.insert_one(myDict)

