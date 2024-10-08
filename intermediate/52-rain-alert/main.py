import requests
from twilio.rest import Client

owm_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "0093a96b010af35e9a47882d48721ab4"
account_sid = "AC71a682495ba7f2fe8c9974bcfd048c7b"
auth_token = "53840fb8770c0b8ae8f2a165c1e4b8bc"

weather_params = {
    "lat": 45.073605,
    "lon": 25.434038,
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
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='+16207431718',
        to='yournr',
        body="Hello"
    )

    print(message.sid)
