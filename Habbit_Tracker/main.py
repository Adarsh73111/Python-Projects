import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = ""
TOKEN = ""
GRAPH_ID = ""

headers = {
    "X-USER-TOKEN": TOKEN
}

today = datetime(year=2026, month=2, day=13).strftime("%Y%m%d")

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

graph_config = {
    "id": GRAPH_ID,
    "name": "Studying Tracker",
    "unit": "Min",
    "type": "float",
    "color": "sora"
}

pixel_data = {
    "date": today,
    "quantity": "420"
}

requests.post(pixela_endpoint, json=user_params)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
requests.post(graph_endpoint, json=graph_config, headers=headers)

pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
response = requests.post(pixel_endpoint, json=pixel_data, headers=headers)

if response.status_code != 200:
    update_endpoint = f"{pixel_endpoint}/{today}"
    requests.put(update_endpoint, json=pixel_data, headers=headers)

delete_endpoint = f"{pixel_endpoint}/{today}"
requests.delete(delete_endpoint, headers=headers)

