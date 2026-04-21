import requests

MY_LAT = 58.602901
MY_LNG = 49.668060
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "#############################"

parameters = {
    "appid": api_key,
    "lat": MY_LAT,
    "lon": MY_LNG,
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for data in weather_data["list"]:
    condition_code = data["weather"][0]["id"]

    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella")