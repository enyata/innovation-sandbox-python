import sys

import requests
import requests
from base64 import b64encode
import base64
from datetime import datetime
import hashlib
import nibss.crypt as crypting




root_url = 'https://innovation-sandbox-backend.herokuapp.com/nibss/'


class Request:

    def __init__(self, code, key, content_type, accept, username, password):
        self.code = str(base64.b64encode(code.encode("utf-8")))
        self.key = key
        self.username = username
        self.password = password
        self.content_type = content_type
        self.accept = accept
        self.sign_meth = 'SHA256'

        auth_string = self.username + ':' + self.password
        self.auth_header = str(base64.b64encode(auth_string.encode("utf-8")))
        date = datetime.today().strftime('YYYYMMDD')
        signature_string = self.username + date + self.password
        self.sign_header = hashlib.sha256(signature_string.encode()).hexdigest()

    # a function to reset sandbox credentials
    def bvn_reset(self):
        headers = {"OrganisationCode": self.code,
                   "Sandbox-Key": self.key}

        response = requests.post(url=root_url + "bvnr/Reset", headers=headers)
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

    # verify single bvn
    def verify_single(self, bvn, aes_key, iv_key):

        headers = {
            # YOUR_ORGANIZATION_CODE_IN_BASE_64
            "OrganisationCode": self.code,
            # YOUR_SANDBOX_KEY
            "Sandbox-Key": self.key,
            "Authorization": self.auth_header,
            "SIGNATURE": self.sign_header,
            "SIGNATURE_METH": self.sign_meth,
            "Content-Type": self.content_type,
            "Accept": self.content_type

        }
        # if self.content_type == 'application/json':
        #     headers

        text = {
            "BVN": bvn
        }
        encrypted = crypting.Crypt().encrypt(text["BVN"], aes_key, iv_key)
        body = {
            encrypted
        }
        try:
            r = requests.post(url=root_url + "bvnr/VerifySingleBVN", headers=headers, data=encrypted)
            # decrypted = crypting.Crypt().decrypt(r, aes_key, iv_key)
            print(r.text)
            return r
        except requests.exceptions.RequestException as e:
            print(e)
            sys.exit(1)

    # verify multiple bvn
    def verify_multiple(self, bvns, aes_key, iv_key):

        headers = {
            # YOUR_ORGANIZATION_CODE_IN_BASE_64
            "OrganisationCode": self.code,
            # YOUR_SANDBOX_KEY
            "Sandbox-Key": self.key,
            "Authorization": self.auth_header,
            "SIGNATURE": self.sign_header,
            "SIGNATURE_METH": self.sign_meth,
            "Content-Type": self.content_type,
            "Accept": self.content_type

        }
        text = {
            "BVNS": bvns
        }
        encrypted = crypting.Crypt().encrypt(text, aes_key, iv_key)
        body = {
            encrypted
        }
        try:
            r = requests.post(url=root_url + "bvnr/VerifyMultipleBVN", headers=headers, data=encrypted)
            decrypted = crypting.Crypt().decrypt(r, aes_key, iv_key)
            return decrypted
        except requests.exceptions.RequestException as e:
            print(e)
            sys.exit(1)

# Request("11111", "8dc1337c1ac82aa90f3bd7b8de8d882a", "application/json", "application/json", "info@enyata.com", "8dco'65T").\
#     verify_single("12345678901", '9+CZaWqfyI/fwezX', "eRpKTBjdOq6T67D0")

    # watchlisted bvn
    def bvn_watchlisted(self, bvn, aes_key, iv_key):

        headers = {
            # YOUR_ORGANIZATION_CODE_IN_BASE_64
            "OrganisationCode": self.code,
            # YOUR_SANDBOX_KEY
            "Sandbox-Key": self.key,
            "Authorization": self.auth_header,
            "SIGNATURE": self.sign_header,
            "SIGNATURE_METH": self.sign_meth,
            "Content-Type": self.content_type,
            "Accept": self.content_type

        }
        text = {
            "BVNS": bvn
        }
        encrypted = crypting.Crypt().encrypt(text["BVNS"], aes_key, iv_key)
        body = {
            encrypted
        }
        try:
            r = requests.post(url=root_url + "bvnr/IsBVNWatchlisted", headers=headers, data=encrypted)
            decrypted = crypting.Crypt().decrypt(r, aes_key, iv_key)
            return decrypted
        except requests.exceptions.RequestException as e:
            print(e)
            sys.exit(1)

    # resetting bvn placeholder
    def bvn_placeholder_reset(self):

        headers = {"OrganisationCode": self.code,
                   "Sandbox-Key": self.key}

        response = requests.post(url=root_url + "BVNPlaceHolder/Reset", headers=headers)
        print(response)

        def placeholder_callback(r):

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

        placeholder_callback(response)

    # finger print verification
    def verify_fingerprint(self, bvn, device_id, reference, finger_type, finger_position, nist, value, aes_key, iv_key):

        headers = {
            # YOUR_ORGANIZATION_CODE_IN_BASE_64
            "OrganisationCode": self.code,
            # YOUR_SANDBOX_KEY
            "Sandbox-Key": self.key,
            "Authorization": self.auth_header,
            "SIGNATURE": self.sign_header,
            "SIGNATURE_METH": self.sign_meth,
            "Content-Type": self.content_type,
            "Accept": self.content_type

        }

        text =  {
          "BVN": bvn,
          "DeviceId": device_id,
          "ReferenceNumber": reference,
          "FingerImage": {
            "type": finger_type,
            "position": finger_position,
            "nist_impression_type": nist,
            "value": value
          }
        }

        encrypted = crypting.Crypt().encrypt(text, aes_key, iv_key)
        try:
            r = requests.post(url=root_url + "bvnr/VerifyFingerPrint", headers=headers, data=encrypted)
            decrypted = crypting.Crypt().decrypt(r, aes_key, iv_key)
            return decrypted
        except requests.exceptions.RequestException as e:
            print(e)
            sys.exit(1)

