import requests
from .response_handler import response
import json


def request(url, payload, headers):
    res = requests.post(url=url, data=payload, headers=headers).json()
    return response(res)


def requestWithParams(url, body, params, headers):
    res = requests.post(url=url, data=json.dumps(
        body), params=params, headers=headers).json()
    return response(res)
