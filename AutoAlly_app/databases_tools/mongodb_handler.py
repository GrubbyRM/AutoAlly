import pymongo
from pymongo.mongo_client import MongoClient
from logging import Logger

class MongoDB():

    def __init__(self):
        self.db = self.connect()
        
    def connect(self):
        try:
            uri = "mongodb+srv://admin:pIG3xrLnm3BlXeoE@autoally.dbtaj5z.mongodb.net/?retryWrites=true&w=majority&appName=AutoAlly"
            self.client = MongoClient(uri)
            db = self.client["AutoAlly"]
            print("Connected to MongoDB")
            return db
            
            
        except Exception as e:
            print(f"Could not connect to MongoDB: {e}")
            
    def get_collection(self, collection_name):
        if self.db is None:
            raise Exception("ERROR. Check MongoDb connection.")
        
        try:
            return self.db[collection_name]
        except Exception as e:
            print("Could not fetch collection. Check collection name.")