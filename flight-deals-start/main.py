import data_manager
import flight_search
from twilio.rest import Client
from datetime import datetime, timedelta
# This file will need to use the DataManager,FlightSearch, FlightData,
# NotificationManager classes to achieve the program requirements.

twilio_sid = "AC2f905bc97a7b11ef3f49d1e6d32f9871"
twilio_token = "73568a93e4cb73316436dd101ff37340"
client = Client(twilio_sid, twilio_token)

sheet = data_manager.DataManager()
sear = flight_search.FlightSearch(sheet)
for city in sear.city_list:
    flight = sear.search(city["iataCode"])
    if flight is None:
        continue
    date = datetime.strptime(flight['local_departure'].split('T')[0],
                             "%Y-%m-%d")+timedelta(days=7)
    flight2 = sear.search_return(city["iataCode"], date)
    date2 = datetime.strptime(flight2['local_departure'].split('T')[0],
                              "%Y-%m-%d")
    price = flight["price"] + flight2["price"]
    if price < city["lowestPrice"]:
        message = client.messages .create(
                     body=f"Low price alert! Only€{price} to fly from {flight['cityFrom']}-{flight['flyFrom']} to {flight['cityTo']}-{flight['flyTo']}, from {date.strftime('%d/%m/%Y')} to {date2.strftime('%d/%m/%Y')}",
                     from_="+19704385554",
                     to='+919781611006'
                 )
