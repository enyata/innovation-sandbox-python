import requests
from .response_handler import response


def request(url, headers):
    res = requests.get(url=url, headers=headers).json()
    return response(res)


def requestWithParams(url, params, headers):
    res = requests.get(url=url, params=params, headers=headers).json()
    return response(res)


def requestWithBody(url, body, headers):
    res = requests.post(url=url, json=body, headers=headers).json()
    return response(res)


def requestWithBodyAndParams(url, body, params, headers):
    res = requests.post(url=url, json=body, params=params,
                        headers=headers).json()
    return response(res)


def requestWithPut(url, body, headers):
    res = requests.put(url=url, json=body, headers=headers).json()
    return response(res)


def requestWithPutAndParams(url, params, body, headers):
    res = requests.put(url=url,  params=params, json=body, headers=headers).json()
    return response(res)
