import os

import requests
import datetime
import os
API_KEY = os.environ.get("API_KEY")
APP_ID = os.environ.get("APP_ID")
endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

user_input = input("Tell me which excercise you did: ")
date = datetime.datetime.now().date().strftime("%d/%m/%y")
time = datetime.datetime.now().time().strftime("%X")
param = {
 "query":user_input,
 "gender":"male",
 "weight_kg":64.2,
 "height_cm":167.64,
 "age":19
}



response = requests.post(endpoint, headers=header, json=param)
response.raise_for_status()
datas = response.json()
datas = datas["exercises"]
print(datas)

SHEET_ENDPOINT = "https://api.sheety.co/9106d6e6510d5f695763b42c92e513e9/myWorkouts/sheet1/7"
for data in  datas:
    update = {
        "sheet1": {
            "date": date,
            "time": time,
            "exercise": data["name"].title(),
            "duration": data["duration_min"],
            "calories": data["nf_calories"]}

    }
    sheety = requests.post(SHEET_ENDPOINT, json=update)
    sheety.raise_for_status()
    print(sheety.text)

# ran = requests.delete(SHEET_ENDPOINT)