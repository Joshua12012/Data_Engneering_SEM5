import requests
from config import weather_api_key

def fetch_weather_data(city):
    url=f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}&units=metric"
    # print("Fetching:", url)   # Debug
    response = requests.get(url)
    return response.json()