import requests

owm_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "0093a96b010af35e9a47882d48721ab4"

weather_params = {
    "lat": 46.744579,
    "lon": 23.484989,
    "appid": api_key,
}

response = requests.get(owm_endpoint, params=weather_params)
print(response.status_code)