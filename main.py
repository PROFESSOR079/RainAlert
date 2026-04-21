import requests

MY_LAT = 41.715137
MY_LNG = 44.827095
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "#############################"

parameters = {
    "appid": api_key,
    "lat": MY_LAT,
    "lon": MY_LNG,
}

response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()
data = response.json()
