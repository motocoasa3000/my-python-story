import requests

owm_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "0093a96b010af35e9a47882d48721ab4"

weather_params = {
    "lat": 46.744579,
    "lon": 23.484989,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(owm_endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
# print(weather_data["list"][0]["weather"][0]["id"])

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    print("Bring an umbrella.")