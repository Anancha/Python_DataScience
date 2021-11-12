from pymongo import MongoClient

client = MongoClient()
client = MongoClient('mongodb://localhost:27017/')

mydb = client['thaivbbiz']
mycol = mydb['product']

data = {
    'ProductID' : '1006',
    'ProductName' : 'พัฒนาเว็บแอพด้วย Vue',
    'ProductPrice' : 315,
    'ProductCost' : 279
}

mydb.product.insert_one(data)

for item in mydb.product.find():
    print(item) 
    print(type(item))
