import requests
from .response_handler import response
import json
import logging

# try:
#     import http.client as http_client
# except ImportError:
#     # Python 2
#     import httplib as http_client
# http_client.HTTPConnection.debuglevel = 1

# # You must initialize logging, otherwise you'll not see debug output.
# logging.basicConfig()
# logging.getLogger().setLevel(logging.DEBUG)
# requests_log = logging.getLogger("requests.packages.urllib3")
# requests_log.setLevel(logging.DEBUG)
# requests_log.propagate = True


def request(url, payload, headers):
    res = requests.post(url=url, data=payload, headers=headers).json()
    return response(res)


def requestWithParams(url, body, params, headers):
    res = requests.post(url=url, data=json.dumps(body), params=params, headers=headers).json()
    return response(res)
