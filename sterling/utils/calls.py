from requests import request, sessions
from sterling.utils.response_handler import response


def calls(method, url, params, data, header):
    try:
        with sessions.Session() as session:
                res = session.request(method= method, url=url, params=params, data=data, headers= header)
                return response(res)
    except Exception as e:
        return e
