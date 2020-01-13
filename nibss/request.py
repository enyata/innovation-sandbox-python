import sys

import requests
import requests
import base64
from datetime import datetime
import hashlib
import nibss.crypt as crypting



root_url = 'https://innovation-sandbox-backend.herokuapp.com/nibss/bvnr/'


class Request:

    def __init__(self, code, key, auth_head, sign, sign_meth, content_type, accept, username, password):
        self.code = code
        self.key = key
        self.username = username
        self.password = password
        self.sign = sign
        self.sign_meth = sign_meth
        self.content_type = content_type
        self.accept = accept

        auth_string = self.username + ':' + self.password
        auth_header = base64(auth_string)
        date = datetime.today().strftime('YYYYMMDD')
        signature_string = self.username + date + self.password
        signature_header = hashlib.sha256(signature_string).digest('hex')

    # a function to reset sandbox credentials
    def reset(self):
        headers = {"OrganisationCode": self.code,
                   "Sandbox-Key": self.key}

        response = requests.post(url=root_url + "Reset", headers=headers)
        print(response)

        def callback(r):

            if r.status_code == 200:
                # print(r.headers)
                data = {
                    "aes_key": r.headers.Aes_key,
                    "password": r.headers.Password,
                    "ivkey": r.headers.Ivkey
                }

            elif r.status_code == 500:
                data = "server error"

            else:
                data = "error"

            print(data)
            return data

        callback(response)

    reset()

    def verify_single(self, bvn):

        headers = {
            # YOUR_ORGANIZATION_CODE_IN_BASE_64
            "OrganisationCode": "MTExMTE=",
            # YOUR_SANDBOX_KEY
            "Sandbox-Key": "8dc1337c1ac82aa90f3bd7b8de8d882a",
            "Authorization": self.auth_header,
            "SIGNATURE": self.sign_header,
            "SIGNATURE_METH": 'SHA256',
            "Content-Type": self.content_type,
            "Accept": self.content_type

        }
        body = {
            "BVN": bvn
        }
        try:
            r = requests.post(url=root_url + "VerifySingleBVN", headers=headers, body=body)
            return r
        except requests.exceptions.RequestException as e:
            print(e)
            sys.exit(1)

    def verify_multiple(self, bvns, aes_key, iv_key):

        headers = {
            # YOUR_ORGANIZATION_CODE_IN_BASE_64
            "OrganisationCode": "MTExMTE=",
            # YOUR_SANDBOX_KEY
            "Sandbox-Key": "8dc1337c1ac82aa90f3bd7b8de8d882a",
            "Authorization": self.auth_header,
            "SIGNATURE": self.sign_header,
            "SIGNATURE_METH": 'SHA256',
            "Content-Type": self.content_type,
            "Accept": self.content_type

        }
        text = {
            "BVNS": bvns
        }
        encrypted = crypting(text.BVNS, aes_key, iv_key)
        body = {
            encrypted
        }
        try:
            r = requests.post(url=root_url + "VerifyMultipleBVN", headers=headers, body=body)
            return r
        except requests.exceptions.RequestException as e:
            print(e)
            sys.exit(1)
