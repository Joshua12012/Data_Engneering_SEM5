import dotenv,os
from dotenv import load_dotenv
load_dotenv()

weather_api_key = os.getenv("WEATHER_API_KEY")

DB_params = {
    "host":f"{os.getenv('HOST')}",
    "database":"weather_reatail_db",
    "user":f"{os.getenv('USER')}",
    "password":f"{os.getenv('PASSWORD')}"
}

cities = [
    {"name":"Delhi"},
    {"name":"Mumbai"},
    {"name":"Pune"},
    {"name":"Lucknow"}
    # {"name":"Banglore"},
    # {"name":"Hydrabad"},
]