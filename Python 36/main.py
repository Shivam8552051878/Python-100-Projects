import requests

param = {
    "appid": "ca2545a4a9e00ad2a677d50ffbde86fb",
    "lat": 6.5244,
    "lon": 72.8777
}

url = f"https://api.openweathermap.org/data/2.5/weather?lat=6.5244&lon=3.3792&appid=ca2545a4a9e00ad2a677d50ffbde86fb"
response = requests.get(url=url, params=param)
data = response.json()
print(data)
