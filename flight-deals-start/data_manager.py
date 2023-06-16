from pickle import NONE
import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.api_id = "https://api.sheety.co/29765f4ac39a389e21d936f9616e0d44/flightDeals/prices"
        self.headers = {
            "Authorization": "Bearer dqwiuhdcqaisbcv"
        }
        self.resp = requests.get(url=self.api_id, headers=self.headers)
        # print(self.resp.json())
