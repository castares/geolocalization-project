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
    json.dumps(r)
    r = requests.get(url, params=params).json()
    #
    # extract = list(map(lambda x: places.append(x), r['results']))
    # while ('next_page_token' in r):
    #     time.sleep(2)
    #     params['pagetoken'] = r['next_page_token']
    #     r = requests.get(url, params=params).json()
    #     extract = list(map(lambda x: places.append(x), r['results']))
    return r


def search_api(target_companies, db, collection, place_type, keyword, radius):
    for e in target_companies:
        longitude = e['geometry']['coordinates'][0]
        latitude = e['geometry']['coordinates'][1]
        answer = nearbyRequest(longitude, latitude,
                               place_type=place_type, keyword=keyword radius=radius)
        for e in answer['results']:
            if e['name'] == 'Starbucks':
                db.collection.insert_one(e)


def main():
    db, offices = comp.connectCollection('companies', 'offices')


if __name__ == "__main__":
    main()
