import requests
from datetime import datetime
MY_LATITUDE = 21.7679
MY_LONGONGITUDE = 78.8718

parameter = {
    "lat":MY_LATITUDE,
    "lng":MY_LONGONGITUDE,
    "formatted":0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameter)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)

current_time = datetime.now().hour
print(current_time)