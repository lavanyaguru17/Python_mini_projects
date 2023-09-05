import requests

# Replace with your OpenWeatherMap API key
api_key = "d0efda27d572be5b7d5733d37e159624"
base_url = "https://api.openweathermap.org/data/2.5/weather"
forecast_url = "https://api.openweathermap.org/data/2.5/forecast"

def get_weather_data(city_name):
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"  # You can change units to "imperial" for Fahrenheit.
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if data.get("main") and data.get("weather"):
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        weather_condition = data["weather"][0]["description"]

        print(f"Weather in {city_name}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
        print(f"Condition: {weather_condition}")

        # Fetch and display forecast data
        forecast_response = requests.get(forecast_url, params=params)
        forecast_data = forecast_response.json()
        forecast_list = forecast_data.get("list")

        if forecast_list:
            print("\nForecast for the next few days:")
            for forecast in forecast_list:
                dt_txt = forecast["dt_txt"]
                temp = forecast["main"]["temp"]
                condition = forecast["weather"][0]["description"]
                print(f"{dt_txt}: {temp}°C, {condition}")
        else:
            print("Forecast data unavailable.")
    else:
        print("City not found or weather data unavailable.")

while True:
    city_name = input("Enter a city name (or 'exit' to quit): ")
    
    if city_name.lower() == "exit":
        break

    get_weather_data(city_name)
