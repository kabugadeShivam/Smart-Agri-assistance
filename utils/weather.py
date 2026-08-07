import os
import requests
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(Path(__file__).parent.parent / ".env")

API_KEY = os.getenv("OPENWEATHER_API_KEY")

print("API KEY:", API_KEY)

def get_weather(city):

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}"
        f"&appid={API_KEY}"
        f"&units=metric"
    )

    print(url)

    response = requests.get(url)

    print("Status Code:", response.status_code)
    print(response.text)

    if response.status_code != 200:
        return None

    data = response.json()

    return {
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "pressure": data["main"]["pressure"],
        "weather": data["weather"][0]["main"],
        "wind": data["wind"]["speed"]
    }