from pymongo import MongoClient

# MongoDB utility class
class MongoHandler(object):
    def __init__(self, host='localhost', port=27017, 
                 database_name=None, collection_name=None) -> None:
        # Connect to a database with given host and port
        try:
            self._client = MongoClient(host=host, port=port)
        except Exception as error:
            raise Exception(error)
        
        self._database = None
        self._collection = None
 
        if database_name:
            self._database = self._client[database_name]
        if collection_name:
            self._collection = self._database[collection_name]
               
    def insert_one(self, post):
        # Add a document to the database
        post_id = self._collection.insert_one(post)
        return post_id

    def insert_many(self, posts_list):
        #Add multiple documents to the database
        post_id = self._collection.insert_many(posts_list)
        return post_id