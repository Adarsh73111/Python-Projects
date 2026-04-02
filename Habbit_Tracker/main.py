# import requests
# from datetime import datetime
#
# pixela_endpoint = "https://pixe.la/v1/users"
# USERNAME = "adarshmisra"
# TOKEN = "123456789"
# GRAPH_ID = "graph26"
#
# user_params = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }
#
# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
#
# graph_config = {
#     "id": GRAPH_ID,
#     "name": "Studying Tracker",
#     "unit": "Min",
#     "type": "float",
#     "color": "sora"
# }
#
# headers = {
#     "X-USER-TOKEN": TOKEN
# }
#
# requests.post(pixela_endpoint, json=user_params)
#
# requests.post(graph_endpoint, json=graph_config, headers=headers)
#
# pixel_creation = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
#
# today = datetime(year=2026, month=2, day=12)
#
# pixel_data = {
#     "date": today.strftime("%Y%m%d"),
#     "quantity": "420"
# }
#
# response = requests.post(pixel_creation, json=pixel_data, headers=headers)
#
# if response.status_code != 200:
#     update_endpoint = f"{pixel_creation}/{today.strftime('%Y%m%d')}"
#     response = requests.put(update_endpoint, json=pixel_data, headers=headers)
#
# print(response.status_code)
# print(response.text)

import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "adarshmisra"
TOKEN = "123456789"
GRAPH_ID = "graph26"

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

