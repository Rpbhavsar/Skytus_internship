import os
import requests
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")


def get_weather(city):
    if not API_KEY:
        print("API key not found. Check your .env file.")
        return

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=params, timeout=10)

        # Show an error instead of crashing when the city/key is invalid
        if response.status_code != 200:
            data = response.json()
            print("Error:", data.get("message", "Unable to get weather"))
            return

        data = response.json()

        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]

        print("\n==== Weather Report ====")
        print("City:", data["name"])
        print("Temperature:", temperature, "°C")
        print("Humidity:", humidity, "%")
        print("Weather:", description)

    except requests.exceptions.RequestException as error:
        print("Connection error:", error)


print("==== Weather App ====")

city = input("Enter a city: ")
get_weather(city)