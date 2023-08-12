import requests
from datetime import datetime

GENDER = "male"
WEIGHT_KG = 62
HEIGHT_CM = 162
AGE = 19

APP_ID = "c6aeb262d37ad159b706b13079b1381f"
API_KEY = "77296f30"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/9106d6e6510d5f695763b42c92e513e9/workout/sheet1"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": API_KEY,
    "x-app-key": APP_ID,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)
################### Start of Step 4 Solution ######################

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "sheet1": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)

    print(sheet_response.text)