import os
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
    r = requests.get(url, params=params)
    return r.json()

def main():
    longitude = -0.208979 
    latitude = 51.51819
    radius=2000
    answer = nearbyRequest(longitude, latitude, radius)
    return answer

if __name__=="__main__":
    main()