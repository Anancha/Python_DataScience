from pymongo import MongoClient

client = MongoClient()
client = MongoClient('mongodb://localhost:27017/')

mydb = client['thaivbbiz']
mycol = mydb['product']

q = {'ProductID' : '1003'}
mycol.delete_one(q)

for item in mydb.product.find():
    print(item)

