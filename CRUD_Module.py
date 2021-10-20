from pymongo import MongoClient

from bson.objectid import ObjectId

from bson.json_util import dumps

class animalShelter(object):
    
    def __init__(self, username = "", password = ""):
        self.username = username
        self.password = password
        self.client = MongoClient('mongodb://%s:%s@localhost:52858/?authMechanism=DEFAULT&authSource=AAC' % (self.username, self.password))
        self.database = self.client.AAC
        self.collection = self.database.animals
        print("Module Initialized")
        
    def create(self, attributes):
        document = attributes
        if document is not []:
            self.collection.insert_one(attributes)
            #print("Create Function")
            return True
        else:
            return False

    def read(self, query):
        result = self.collection.find(query)
        if result is None:
            raise Exception("No object found")
        else:
            #print("Read Function")
            return result
        
    def update(self, query, updates):
        self.collection.update_one(query, updates)
        result = self.collection.find(query)
        list_cur = list(result)
        json_data = dumps(list_cur)
        #print("Update Function")
        return json_data
    
    def delete(self, query):
        docToDelete = self.collection.find(query)
        if docToDelete is None:
            raise Exception("No object to delete")
        else:
            self.collection.delete_one(query)
        list_cur = list(docToDelete)
        json_data = dumps(list_cur)
        #print("Delete function")
        return json_data
    