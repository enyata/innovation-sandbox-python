import requests
from .response_handler import response


def request(url, payload, headers):
    res = requests.post(url=url, data=payload, headers=headers).json()
    return response(res)