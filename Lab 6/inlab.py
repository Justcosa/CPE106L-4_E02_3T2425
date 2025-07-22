from pymongo import MongoClient
import pprint
import re

# client = MongoClient(host="localhost", port=27017)
client = MongoClient(host="mongodb://localhost:27017")

#Get reference to 'chinook' database
db = client["chinook"]

#Get reference to 'customers' collection
customers_collection = db["customers"]

#print first document
docl = customers_collection.find_one()
print(docl)

client.close()
