from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

## Calls the Open Weather API and returns the JSON data for queried city
def get_current_weather(city="Bengaluru"):
    request_url = f'http://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'
    weather_data = requests.get(request_url).json()
    return weather_data