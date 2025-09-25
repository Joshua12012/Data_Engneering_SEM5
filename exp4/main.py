import time
from config import cities
from db import get_connection,create_table
from fetch import fetch_weather_data, create_json_file
from insert import insert_weather

def main():
    connection,cursor = get_connection()
    create_table(cursor,connection)
    
    while True:
        for city in cities:
            data = fetch_weather_data(city['name'])
            if data:
                insert_weather(cursor,connection,data)
        print("Batch completed, sleeping for 10 seconds")
        time.sleep(10)
        
if __name__=="__main__":
    main()