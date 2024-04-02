import pymongo

#creating database
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["sandrik"]

#creating structure
mycol = mydb["customers"]

#insert data
mydict = { "name": {"John":"hi","hi":"look"}, "address": "Highway 37" }
x = mycol.insert_one(mydict)
mydict = { "name": "John", "address": "Highway 37" }
x = mycol.insert_one(mydict)

#query
myquery = { "address": "leselidze" }
mydoc = mycol.find(myquery)


#sort
mydoc = mycol.find().sort("name")
 
#delete
myquery = { "address": "Mountain 21" }
mycol.delete_one(myquery)

#drop
#mycol.drop()

#update
myquery = { "address": "leselidze" }
newvalues = { "$set": { "address": "Canyon 123" } }
mycol.update_one(myquery, newvalues)
#print "customers" after the update:
for x in mycol.find():
  print(x)