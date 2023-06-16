import datetime as dt
import pandas
from random import randint
import smtplib
# ##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
data = pandas.read_csv("birthdays.csv")
data = data.to_dict(orient="records")

ran = randint(1, 3)
letter_location = f"letter_templates/letter_{ran}.txt"

my_email = "smtptestemail.0.1.2.3@gmail.com"
password = "jxispuyyfswnpeyv"
connection = smtplib.SMTP("smtp.gmail.com", 587)
connection.starttls()
connection.login(user=my_email, password=password)

for person in data:
    if person["day"] == now.day and person["month"] == now.month:
        name = person["name"]
# 3. If step 2 is true, pick a random letter from letter templates and replace
# the [NAME] with the person's actual name from birthdays.csv
        with open(letter_location) as letter:
            content = letter.readlines()
            content[0] = content[0].replace("[NAME]", f"{name}")
        letter_content = " ".join(content)
        connection.sendmail(from_addr=my_email, to_addrs=person['email'],
                            msg="Subject: Happy Birthday \n\n"+letter_content)
# 4. Send the letter generated in step 3 to that person's email address.
connection.close()
