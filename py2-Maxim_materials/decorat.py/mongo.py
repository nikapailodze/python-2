import pymongo
import job

Myclient=pymongo.MongoClient("mongodb://localhost:27017")
mydb=Myclient["GEO_Celebs"]
mycol=mydb["friends"]

fr1=job.fr_1

# mydict={"name":fr1.name,"surname":fr1.surname}

# mycol.insert_one(mydict)

query={"name":fr1.name}
newvalue= {"$set" :{"age":fr1.age}}

mycol.update_many(query,newvalue)