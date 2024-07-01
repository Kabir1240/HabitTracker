import requests
import os
from datetime import datetime

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ENDPOINT = "/<username>/graphs"
POST_PIXEL_ENDPOINT = "/<username>/graphs/<graphID>"
UPDATE_PIXEL_ENDPOINT = "/<username>/graphs/<graphID>/<yyyyMMdd>"
DELETE_PIXEL_ENDPOINT = "/<username>/graphs/<graphID>/<yyyyMMdd>"
DELETE_GRAPH_ENDPOINT = "/<username>/graphs/<graphID>"
TOKEN = os.environ['TOKEN']

def create_user(username:str) -> None:
    user_params = \
        {
            "token": TOKEN,
            "username": username,
            "agreeTermsOfService": "yes",
            "notMinor": "yes",
        }

    endpoint = PIXELA_ENDPOINT
    response = requests.post(url=endpoint, json=user_params)
    print(response.text)


def create_graph(username:str, graph_name:str, unit:str, color:str) -> None:
    headers = \
        {
            "X-USER-TOKEN": TOKEN,
        }

    user_params = \
        {
            "id": "graph1",
            "name": graph_name,
            "unit": unit,
            "type": "float",
            "color": color,
        }

    endpoint = PIXELA_ENDPOINT + GRAPH_ENDPOINT.replace("<username", username)
    response = requests.post(url=endpoint, json=user_params, headers=headers)
    print(response.text)


def post_pixel(username:str, graph_id:str, quantity:str) -> None:
    headers = \
        {
            "X-USER-TOKEN": TOKEN,
        }

    date_today = datetime.now().strftime("%Y%m%d")
    user_params = \
        {
            "date": date_today,
            "quantity": quantity,
        }

    endpoint = PIXELA_ENDPOINT + POST_PIXEL_ENDPOINT.replace("<username>", username).replace("<graphID>", graph_id)
    response = requests.post(url=endpoint, json=user_params, headers=headers)
    print(response.text)


def update_pixel(username:str, graph_id:str, new_quantity:str) -> None:
    headers = \
        {
            "X-USER-TOKEN": TOKEN,
        }

    user_params = \
        {
            "quantity": new_quantity,
        }

    date_today = datetime.now().strftime("%Y%m%d")

    endpoint = (PIXELA_ENDPOINT + UPDATE_PIXEL_ENDPOINT.replace("<username>", username)
                .replace("<graphID>", graph_id).replace("<yyyyMMdd>", date_today))
    response = requests.put(url=endpoint, headers=headers, json=user_params)
    print(response.text)


def delete_pixel(username:str, graph_id:str) -> None:
    headers = \
        {
            "X-USER-TOKEN": TOKEN,
        }

    date_today = datetime.now().strftime("%Y%m%d")

    endpoint = (PIXELA_ENDPOINT + DELETE_PIXEL_ENDPOINT.replace("<username>", username)
                .replace("<graphID>", graph_id).replace("<yyyyMMdd>", date_today))
    response = requests.delete(url=endpoint, headers=headers)
    print(response.text)


def delete_graph(username:str, graph_id:str) -> None:
    headers = \
        {
            "X-USER-TOKEN": TOKEN,
        }

    endpoint = PIXELA_ENDPOINT + DELETE_GRAPH_ENDPOINT.replace("<username>", username).replace("<graphID>", graph_id)
    response = requests.delete(url=endpoint, headers=headers)
    print(response.text)
