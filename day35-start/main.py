from urllib import response
import requests
from twilio.rest import Client

API_KEY = "9bcaa35f79f8a7b003c926222e28a164"
MY_LAT = 17.497320
MY_LONG = 78.398613
OWN_ENDPOINT = "https://api.openweathermap.org/data/3.0/onecall"

account_sid = "AC2f905bc97a7b11ef3f49d1e6d32f9871"
auth_token = "73568a93e4cb73316436dd101ff37340"
client = Client(account_sid, auth_token)

weather_params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "exclude": ["current,minutely,daily,alerts"]
}
resp = requests.get(OWN_ENDPOINT, params=weather_params)
resp.raise_for_status()
hourly_data = resp.json()["hourly"][:12]
id_data = [hour["weather"][0]["id"] for hour in hourly_data]
for i in id_data:
    if i < 700:
        print("Bring an umbrella")
        message = client.messages.create(
                              body="It is going to raain today. Remeber to bring an umbrella ☔️",
                              from_='+19704385554',
                              to='+919781611006'
                          )
        print(message.status)
        break
