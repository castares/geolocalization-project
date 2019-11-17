from pymongo import MongoClient

def connectCollection(database, collection):
    #connects to a mongodb using pymongo 
    #and returns a given collection from a given database.
    client = MongoClient()
    db = client[database]
    coll = db[collection]
    return db, coll

def target_offices(country_code, foundation_year, money_raised):
        return list(offices.find({
            "$and" : [
                {"properties.country":f"{country_code}"}, 
                {"properties.foundation_year": {"$gt": foundation_year}}, 
                {"properties.company_money_raised" : {"$gte" :f"${money_raised}M"}}
            ]
        }))

def near_offices(geometry, max_distance=2000):
    #Finds values in the offices companies.offices collection 
    #matching the given geometry and distance in meters values.
    return list(offices.find({"geometry.coordinates": 
        {"$near" : 
             {
            "$geometry": geometry ,
            "$maxDistance": max_distance
        }}
    }))

def old_companies(offices, year):
    #Given a list of companies, returns the ones founded before the given year.
    old_companies = []
    for office in offices: 
        if office['properties']['foundation_year'] < year:
            old_companies.append(office)
    return old_companies

    

def main():
    pass


if __name__=="__main__":
    main()