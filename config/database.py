from pymongo.mongo_client import MongoClient

url = "mongodb+srv://omoyenidavidoluwayinka:Omoyenido17@cluster0.u5eop.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(url)
db = client.todo_application

collection_name  = db["todos_app"]
