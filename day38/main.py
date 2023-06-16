import requests
from datetime import datetime

API_KEY = "4f0a5bac3eb57fbf2899259c41b2c0ba"
APP_ID = "3934b19c"
API_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = "https://api.sheety.co/a39ace73d16667f8479ba5d57a67bd1b/myWorkouts/workouts"
SHEETY_TOKEN = "vsdiojvnovsnol"


exercise = input("Tell me which exercises you did\n")
now = datetime.now()
time = now.time().strftime("%H:%M:%S")
params = {
    "query": exercise
}


headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0",
}
resp = requests.post(url=API_ENDPOINT, json=params, headers=headers)
data = resp.json()["exercises"]

sheety_headers = {
    "Authorization": "Bearer vsdiojvnovsnol",
}

for exercise in data:
    post_params = {
        "workout": {
            "date": now.date().strftime("%d/%m/%Y"),
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
    post_resp = requests.post(url=SHEETY_ENDPOINT, json=post_params,
                              headers=sheety_headers)
    print(post_resp.text)
