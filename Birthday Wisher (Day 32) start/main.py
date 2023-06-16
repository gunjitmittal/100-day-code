import smtplib
import datetime as dt
from random import choice
file = open("quotes.txt")
quotes = file.readlines()
file.close()
now = dt.datetime.now()
weekday = now.weekday()
my_email = "smtptestemail.0.1.2.3@gmail.com"
password = "jxispuyyfswnpeyv"
connection = smtplib.SMTP("smtp.gmail.com", 587)
connection.starttls()
connection.login(user=my_email, password=password)
print(weekday)
if weekday == 1:
    quote = choice(quotes)
    connection.sendmail(from_addr=my_email, to_addrs="gunjitmittal2@gmail.com",
                        msg=f"Subject: Keep up the good work \n\n {quote}")
connection.close()
