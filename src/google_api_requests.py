import os
import time
import requests
import json
from dotenv import load_dotenv

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

def nearbyRequest(longitude, latitude, place_type, keyword, rankby='distance'):
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?"
    params = {
        'location': f'{latitude},{longitude}',
        'type': place_type,
        'keyword': keyword,
        'rankby': rankby,
        'key': api_key
    }
    places = []
    r = requests.get(url, params=params).json()
    # extract = list(map(lambda x: places.append(x), r['results']))
    # while ('next_page_token' in r):
    #     time.sleep(2)
    #     params['pagetoken'] = r['next_page_token']
    #     r = requests.get(url, params=params).json()
    #     extract = list(map(lambda x: places.append(x), r['results']))
    return r


def main():
    longitude = -0.2058693
    latitude = 51.5153986
    keyword = 'Starbucks'
    place_type = 'cafe'
    places = nearbyRequest(longitude, latitude, place_type, keyword)

    # print(places)


if __name__ == "__main__":
    main()
