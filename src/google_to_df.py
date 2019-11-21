import pandas as pd
import companiesdb as comp


def getLocation(item):
    longitude = item['geometry']['location']['lng']
    latitude = item['geometry']['location']['lat']
    loc = {
        'type': 'Point',
        'coordinates': [float(longitude), float(latitude)]
    }
    return loc


def nearTo(offices, geometry, max_distance=2000):
    # Finds values in the offices companies.offices collection
    # matching the given geometry and distance in meters values.
    return list(offices.find({"geometry.coordinates": {"$near": {"$geometry": geometry,
                                                                 "$maxDistance": max_distance
                                                                 }}
                              }))


def addLocation(coll):
    db, collection = comp.connectCollection("companies", coll)
    items = list(collection.find())
    for item in items:
        value = {"$set": {'location': getLocation(item)}}
        collection.update_one(item, value)
    #collection.ensure_index(["location.coordinates", "GEO2D"])


def main():
    df = pd.read_csv('../output/ranking.csv')
    # addLocation('starbucks')
    addLocation('bars')
    addLocation('airports')
    addLocation('schools')


if __name__ == "__main__":
    main()
