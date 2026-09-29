import requests

def get_weather(city):
    api_key = "39383c1306fd7ae85cc233b5a98fea2d"

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=params)

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

city = input("Enter a city:")
get_weather(city)