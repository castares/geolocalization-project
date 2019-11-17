from pymongo import MongoClient

def connectCollection(database, collection):
    #connects to a mongodb using pymongo 
    #and returns a given collection from a given database.
    client = MongoClient()
    db = client[database]
    coll = db[collection]
    return db, coll




def main():
    pass


if __name__=="__main__":
    main()