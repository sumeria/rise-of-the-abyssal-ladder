import requests
import pymongo
from datetime import datetime
import time

MONGO_URI = "mongodb://localhost:27017/"
DB_NAME = "poe_ladder"
COLLECTION_NAME = "rise_of_abyssal"
API_URL = "https://pathofexile2.com/internal-api/content/game-ladder/id/Rise%20of%20the%20Abyssal"

client = pymongo.MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'Accept': 'application/json, text/plain, */*',
    'Referer': 'https://pathofexile2.com/',
}

def fetch_and_store():
    response = requests.get(API_URL, headers=headers)
    if response.status_code == 200:
        data = response.json()
        data['fetched_at'] = datetime.utcnow()
        collection.insert_one(data)
        print(f"Stored data at {data['fetched_at']}")
    else:
        print("Failed to fetch data:", response.status_code)

if __name__ == "__main__":
    while True:
        fetch_and_store()
        time.sleep(300)  # Wait 5 minutes

