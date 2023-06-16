import requests
from datetime import datetime

now = datetime.now()
date = now.strftime("%Y%m%d")
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = "ramanujaducks"
TOKEN = "mnj4oadnc1aod0jfnao5dac"
graph_endpoint = PIXELA_ENDPOINT+f"/{USERNAME}/graphs"
graph1_endpoint = graph_endpoint+"/graph1"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

graph_params = {
    "id": "graph1",
    "name": "Python progress",
    "unit": "Days",
    "type": "int",
    "color": "sora"
}

graph1_params = {
    "date": date,
    "quantity": "3"
}

graph1_change_params = {
    "quantity": "4"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# resp = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(resp.text)

# graph_resp = requests.post(url=graph_endpoint,
#                            json=graph_params, headers=headers)
# print(graph_resp.text)

# graph1_resp = requests.post(url=graph1_endpoint,
#                             json=graph1_params, headers=headers)
# print(graph1_resp.text)

# graph1_change = requests.put(url=graph1_endpoint+f"/{date}",
#                              json=graph1_change_params, headers=headers)
# print(graph1_change.text)

graph1_delete = requests.delete(url=graph1_endpoint+f"/{date}",
                                headers=headers)
