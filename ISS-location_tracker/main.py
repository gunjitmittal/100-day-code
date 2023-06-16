from time import sleep
import requests
from datetime import datetime
import smtplib

MY_LAT = 17.497320
MY_LONG = 78.398613
parameters = {
    "lat": MY_LAT,
    "long": MY_LONG,
    "formatted": 0
}
my_email = "smtptestemail.0.1.2.3@gmail.com"
password = "jxispuyyfswnpeyv"

iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
iss_response.raise_for_status()
iss_data = iss_response.json()
iss_lat = iss_data["iss_position"]["latitude"]
iss_long = iss_data["iss_position"]["longitude"]

response = requests.get(url="https://api.sunrise-sunset.org/json",
                        params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
time_now = datetime.now()

while True:
    if (time_now.hour > sunset or time_now.hour < sunrise) and (abs(iss_lat-MY_LAT) < 5 and abs(iss_long-MY_LONG) < 5):
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="gunjitmittal2@gmail.com",
                                msg="Subject: ISS above you \n\n Look"
                                "into the sky and you should be able"
                                "to spot the ISS")
    sleep(60)
