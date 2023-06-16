import imp
import math
from time import strftime
import requests
import data_manager
from datetime import datetime, timedelta


class FlightSearch():
    # This class is responsible for talking to the Flight Search API.
    def __init__(self, data: data_manager.DataManager):
        self.api_endpoint = "https://tequila-api.kiwi.com/locations/query"
        self.search_api_point = "https://tequila-api.kiwi.com/v2/search"
        self.head = {
            "apikey": "vABtHc71pqeV2UkQbkYcOgT4OKOp5DAG"
        }
        for city in data.resp.json()["prices"]:
            params = {
                "term": city["city"],
                "location_types": "city"
            }
            self.resp = requests.get(url=self.api_endpoint, params=params,
                                     headers=self.head)
            code = self.resp.json()["locations"][0]["code"]
            city["iataCode"] = code
            update_params = {
                "price": {
                    "iataCode": code
                }
            }
        self.city_list = data.resp.json()["prices"]

    def search(self, city):
        now = datetime.now()
        month6 = now + timedelta(days=180)
        search_params = {
            "fly_from": "LON",
            "fly_to": city,
            "date_from": now.strftime("%d/%m/%Y"),
            "date_to": month6.strftime("%d/%m/%Y")
        }
        resp = requests.get(url=self.search_api_point,
                            params=search_params, headers=self.head)
        try:
            data = resp.json()["data"][0]
        except IndexError:
            return None
        else:
            min_price = math.inf
            for flight in resp.json()["data"]:
                price = flight["price"]
                if price < min_price:
                    min_price = price
                    min_flight = flight
            return min_flight

    def search_return(self, city, date):
        month6 = date + timedelta(days=21)
        search_params = {
            "fly_from": city,
            "fly_to": "LON",
            "date_from": date.strftime("%d/%m/%Y"),
            "date_to": month6.strftime("%d/%m/%Y")
        }
        resp = requests.get(url=self.search_api_point,
                            params=search_params, headers=self.head)
        min_price = math.inf
        for flight in resp.json()["data"]:
            price = flight["price"]
            if price < min_price:
                min_price = price
                min_flight = flight
        return min_flight
