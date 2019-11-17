import os
import time
import requests
import json
from dotenv import load_dotenv

load_dotenv()
#API authentication
api_key = os.getenv("GOOGLE_CLOUD_API_KEY")

def nearbyRequest(longitude, latitude, radius):
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?"
    params = {
        'location' : f'{latitude},{longitude}',
        'radius' : radius,
        'key' : api_key
    }
    answers = []
    r = requests.get(url, params=params).json()
    answers.append(r)
    while ('next_page_token' in r):
        time.sleep(2)
        params['pageToken'] = r['next_page_token']
        r = requests.get(url, params=params).json()
        answers.append(r)
    print(answers)
    return answers

def main():
    longitude = -0.208979 
    latitude = 51.51819
    radius=200
    return nearbyRequest(longitude, latitude, radius)

if __name__=="__main__":
    main()