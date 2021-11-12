from pymongo import MongoClient

client = MongoClient()
client = MongoClient('mongodb://localhost:27017/')

mydb = client['thaivbbiz']
mycol = mydb['product']

q = {'ProductID' : '1002'}
newdata = {"$set" : {'ProductCost' : 200}}

mycol.update_one(q, newdata)

for item in mydb.product.find():
    print(item)

