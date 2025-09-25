import requests
import json
from config import weather_api_key

def fetch_weather_data(city):
    url=f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()
        create_json_file(data)
        return data
    except requests.RequestException as e:
        print(f"Failed to fetch weather api for {city} city")
        return None

def create_json_file(data):
    with open("weather_json.json","w") as file:
        json.dump(data, file, indent=4)