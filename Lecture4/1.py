import pymongo


client = pymongo.MongoClient("mongodb://localhost:27017")
myDb= client["nikas_Db"]

mycol=myDb["Friends"]

# mydict={"name":"Maiko", "Surname": "Giorgadze" ,"address": "Tsereteli"}
# mycol.insert_one(mydict)
# mydict={"name":"Tekle", "Surname": "Chankvetadze" ,"address": "Sofeli-Dighomi"}
# mycol.insert_one(mydict)
# mydict={"name":"Nuki", "Surname": "koshkel/Mshvidi" ,"address": "Temqa/Gvetadze"}



# # Data Insertion
# mycol.insert_one(mydict)

# mydict={"name":"ketrinaga", "Surname": "Gaboidi" ,"address": "Gabexebtan"}
# mycol.insert_one(mydict)

# Printing Data

# for x in mycol.find():
#     print(x)

# Finding Data


# myquery={"name": "Nuki"}
# mydoc=mycol.find(myquery)

# for result in mydoc:
#     print(result["name"])

# without loop
    
# result= mycol.find_one({"name":"Maiko"})
# print(result)





# Delete Data
# myquery={"address":"kavtaradze"}
# mycol.delete_many(myquery)
    


#Update 

# result= mycol.update_one({"name":"Tekle"}, {"$set":{"name":"Teklachki"}})

# currValue={"name":"Teklakukla"}
# newValue={"$set":{"Les": "Boseli"}}

# mycol.update_one(currValue,newValue)



# currValue={"name":"ketrinaga"}
# newValue={"$set":{"Pet":"Miso_Gaboidi"}}

# mycol.update_one(currValue,newValue)


# Setting id

# ider=1
# for resutlt in mycol.find():
#     print(resutlt["name"])
    
#     currValue=resutlt
#     newValue={"$set": {"identifier":ider}}
#     mycol.update_one(currValue,newValue)
#     ider+=1
