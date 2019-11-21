import os
import time
import requests
import json
from dotenv import load_dotenv
import companiesdb as comp

load_dotenv()

# API authentication
api_key = os.getenv("GOOGLE_CLOUD_API_KEY")


# def nearbyRequest(longitude, latitude, radius, place_type):
#     url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?"
#     params = {
#         'location': f'{latitude},{longitude}',
#         'radius': radius,
#         'key': api_key,
#         'type': place_type
#     }
#     places = []
#     r = requests.get(url, params=params).json()
#     extract = list(map(lambda x: places.append(x), r['results']))
#     while ('next_page_token' in r):
#         time.sleep(2)
#         params['pagetoken'] = r['next_page_token']
#         r = requests.get(url, params=params).json()
#         extract = list(map(lambda x: places.append(x), r['results']))
#     return places

def nearbyRequest(longitude, latitude, place_type, keyword, radius):
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?"
    params = {
        'location': f'{latitude},{longitude}',
        'type': place_type,
        'keyword': keyword,
        'radius': radius,
        'key': api_key
    }
    res = requests.get(url, params=params).json()
    #
    # extract = list(map(lambda x: places.append(x), r['results']))
    # while ('next_page_token' in r):
    #     time.sleep(2)
    #     params['pagetoken'] = r['next_page_token']
    #     r = requests.get(url, params=params).json()
    #     extract = list(map(lambda x: places.append(x), r['results']))
    return res


def searchbyRadius(target_companies, db, collection, place_type, keyword, radius):
    for e in target_companies:
        longitude = e['geometry']['coordinates'][0]
        latitude = e['geometry']['coordinates'][1]
        answer = nearbyRequest(longitude, latitude,
                               place_type=place_type, keyword=keyword, radius=radius)
        print('Request done')
        for x in answer['results']:
            geoJSON = {
                "type": "Feature",
                "geometry": {
                        "type": "Point",
                        "coordinates": [float(x['geometry']['location']['lng']),
                                        float(x['geometry']['location']['lat'])]
                },
                "properties": {
                    "name": x["name"],
                    "id": x["id"],
                    "reference": e["properties"]["name"]}
            }
            db[collection].insert_one(geoJSON)
            print("document inserted")


def main():
    # search starbucks near the list of  target offices and update the results
    # on a mongo collection.
    db, coll = comp.connectCollection("companies", "offices")
    target = json.load(open('../output/target_offices.json'))
    searchbyRadius(target, db, "schools", 'school', 'school', 1000)
    searchbyRadius(target, db, "starbucks", 'cafe', 'starbucks', 500)
    searchbyRadius(target, db, "airports", 'airport', 'airport', 5000)
    searchbyRadius(target, db, "bars", 'night_club', 'night_club', 1000)


if __name__ == "__main__":
    main()
