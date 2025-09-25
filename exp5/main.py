import time
from db import get_mongo_connection
from fetch_weather import fetch_weather_data
from insert import insert_weather
from config import cities

def main():
    while True:
        collection = get_mongo_connection()
        
        for city in cities:
            weather_data = fetch_weather_data(city['name'])
            insert_weather(collection,weather_data,city)
        time.sleep(20)
    
if __name__=="__main__":
    main()