from flask import Flask
from flask_pymongo import PyMongo

class MongoDB:
    def __init__(self, app):
        username = "cipasoft"
        password = "cipasoft2023"
        cluster = "cluster0.xongah3.mongodb.net"
        database = "autonomus"
        
        uri = f"mongodb+srv://{username}:{password}@{cluster}/{database}?retryWrites=true&w=majority"
        app.config['MONGO_URI'] = uri

        self.mongo = PyMongo(app)

    def get_connection(self):
        return self.mongo.cx

    def get_db(self):
        return self.mongo.db
    
app = Flask(__name__)
mongo = MongoDB(app)
