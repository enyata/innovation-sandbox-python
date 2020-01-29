import requests
from nibss.utils import crypt as crypting
from nibss.utils.error_handler import error


def request(head, url):
    r = requests.post(url=url, headers=head)
    if r.status_code == 200:
        data = {
            "aes_key": r.headers['Aes_key'],
            "password": r.headers['Password'],
            "ivkey": r.headers['Ivkey']
        }
    else:
        data = error(r.status_code)
    return data


def encrypted_request(head, url, aes, iv, body):
    encrypted = crypting.Crypt().encrypt(body, aes, iv)
    try:
        r = requests.post(url=url, headers=head, data=encrypted)
        if r.status_code == 200:
            data = crypting.Crypt().decrypt(r.text, aes, iv)
        else:
            data = error(r.status_code)
        return data
    except requests.exceptions.RequestException as e:
        return e
        sys.exit(1)

