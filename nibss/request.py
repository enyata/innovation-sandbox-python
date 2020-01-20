import base64
import hashlib
import sys
import arrow
import requests
import nibss.crypt as crypting
from urllib.parse import urljoin
from nibss.url import url as BASE_URL


class Request:
    def __init__(self, util_dict):
        self.util_dict = util_dict
        self.url = self.util_dict["base_url"]
        self.key = self.util_dict["sandbox-key"]
        self.content_type = self.util_dict["content-type"]
        self.accept = self.util_dict["accept"]
        self.code = (base64.b64encode(self.util_dict["Organizationcode"].encode("utf-8"))).decode('utf8')
        self.sign_meth = 'SHA256'
        auth_string = self.util_dict["username"] + ':' + self.util_dict["password"]
        self.auth_header = (base64.b64encode(auth_string.encode("utf-8"))).decode('utf8')
        datenow = arrow.now().format('YYYY-MM-DD').split('-')
        date = ''.join(datenow)
        signature_string = self.util_dict["username"] + str(date) + self.util_dict["password"]
        self.sign_header = hashlib.sha256(signature_string.encode('utf-8')).hexdigest()

    def get_params(self):
        return self.util_dict

        # a function to reset sandbox credentials

    def bvn_reset(self):
        headers = {
            "OrganisationCode": self.code,
            "Sandbox-Key": self.key
        }
        URL = urljoin(BASE_URL(self.url), "/nibss/bvnr/Reset")
        response = requests.post(url=URL, headers=headers)

        def callback(r):
            if r.status_code == 200:
                data = {
                    "aes_key": r.headers['Aes_key'],
                    "password": r.headers['Password'],
                    "ivkey": r.headers['Ivkey']
                }
            elif r.status_code == 500:
                data = "server error"
            elif r.status_code == 403:
                data = "Expired Sandbox Key"
            else:
                data = "error"
            return data

        t = callback(response)
        return t

    # verify single bvn
    def verify_single(self, body, aes_key, iv_key):
        URL = urljoin(BASE_URL(self.url), "/nibss/bvnr/VerifySingleBVN")
        headers = {
            "OrganisationCode": self.code,
            "Sandbox-Key": self.key,
            "Authorization": self.auth_header,
            "SIGNATURE": self.sign_header,
            "SIGNATURE_METH": self.sign_meth,
            "Content-Type": self.content_type,
            "Accept": self.accept
        }
        encrypted = crypting.Crypt().encrypt(body, aes_key, iv_key)

        try:
            r = requests.post(url=URL, headers=headers, data=encrypted)
            if r.status_code == 200:
                data = crypting.Crypt().decrypt(r.text, aes_key, iv_key)
            elif r.status_code == 500:
                data = "server error"
            elif r.status_code == 403:
                data = "Expired Sandbox Key"
            else:
                data = "error"
            return data
        except requests.exceptions.RequestException as e:
            return e
            sys.exit(1)

    # verify multiple bvn
    def verify_multiple(self, bvns, aes_key, iv_key):
        URL = urljoin(BASE_URL(self.url), "/nibss/bvnr/VerifyMultipleBVN")
        headers = {
            "OrganisationCode": self.code,
            "Sandbox-Key": self.key,
            "Authorization": self.auth_header,
            "SIGNATURE": self.sign_header,
            "SIGNATURE_METH": self.sign_meth,
            "Content-Type": self.content_type,
            "Accept": self.accept
        }
        body = bvns
        encrypted = crypting.Crypt().encrypt(body, aes_key, iv_key)

        try:
            r = requests.post(url=URL, headers=headers, data=encrypted)
            if r.status_code == 200:
                data = crypting.Crypt().decrypt(r.text, aes_key, iv_key)
            elif r.status_code == 500:
                data = "server error"
            elif r.status_code == 403:
                data = "Expired Sandbox Key"
            else:
                data = "error"
            return data
        except requests.exceptions.RequestException as e:
            return e
            sys.exit(1)

    def bvn_watchlisted(self, body, aes_key, iv_key):
        URL = urljoin(BASE_URL(self.url), "/nibss/bvnr/IsBVNWatchlisted")
        headers = {
            "OrganisationCode": self.code,
            "Sandbox-Key": self.key,
            "Authorization": self.auth_header,
            "SIGNATURE": self.sign_header,
            "SIGNATURE_METH": self.sign_meth,
            "Content-Type": self.content_type,
            "Accept": self.content_type
        }
        encrypted = crypting.Crypt().encrypt(body, aes_key, iv_key)

        try:
            r = requests.post(url=URL, headers=headers, data=encrypted)
            if r.status_code == 200:
                data = crypting.Crypt().decrypt(r.text, aes_key, iv_key)
            elif r.status_code == 500:
                data = "server error"
            elif r.status_code == 403:
                data = "Expired Sandbox Key"
            else:
                data = "error"
            return data
        except requests.exceptions.RequestException as e:
            return e
            sys.exit(1)

    # resetting bvn placeholder
    def bvn_placeholder_reset(self):
        URL = urljoin(BASE_URL(self.url), "/nibss/BVNPlaceHolder/Reset")
        headers = {
            "OrganisationCode": self.code,
            "Sandbox-Key": self.key
        }

        response = requests.post(url=URL, headers=headers)

        def placeholder_callback(r):
            if r.status_code == 200:
                data = {
                    "aes_key": r.headers['Aes_key'],
                    "password": r.headers['Password'],
                    "ivkey": r.headers['Ivkey']
                }
            elif r.status_code == 500:
                data = "server error"
            elif r.status_code == 403:
                data = "Expired Sandbox Key"
            else:
                data = "error"
            return data

        t = placeholder_callback(response)
        return t

    # validate record
    def validate_record(self, body, aes_key, iv_key):
        URL = urljoin(BASE_URL(self.url), "/nibss/BVNPlaceHolder/ValidateRecord")
        headers = {
            "OrganisationCode": self.code,
            "Sandbox-Key": self.key,
            "Authorization": self.auth_header,
            "SIGNATURE": self.sign_header,
            "SIGNATURE_METH": self.sign_meth,
            "Content-Type": self.content_type,
            "Accept": self.content_type
        }
        encrypted = crypting.Crypt().encrypt(body, aes_key, iv_key)

        try:
            r = requests.post(url=URL, headers=headers, data=encrypted)
            if r.status_code == 200:
                data = crypting.Crypt().decrypt(r.text, aes_key, iv_key)
            elif r.status_code == 500:
                data = "server error"
            elif r.status_code == 403:
                data = "Expired Sandbox Key"
            else:
                data = "error"
            return data
        except requests.exceptions.RequestException as e:
            return e
            sys.exit(1)

    # validate records
    def validate_records(self, body, aes_key, iv_key):
        URL = urljoin(BASE_URL(self.url), "/nibss/BVNPlaceHolder/ValidateRecords")
        headers = {
            "OrganisationCode": self.code,
            "Sandbox-Key": self.key,
            "Authorization": self.auth_header,
            "SIGNATURE": self.sign_header,
            "SIGNATURE_METH": self.sign_meth,
            "Content-Type": self.content_type,
            "Accept": self.content_type
        }
        encrypted = crypting.Crypt().encrypt(body, aes_key, iv_key)

        try:
            r = requests.post(url=URL, headers=headers, data=encrypted)
            if r.status_code == 200:
                data = crypting.Crypt().decrypt(r.text, aes_key, iv_key)
            elif r.status_code == 500:
                data = "server error"
            elif r.status_code == 403:
                data = "Expired Sandbox Key"
            else:
                data = "error"
            return data
        except requests.exceptions.RequestException as e:
            return e
            sys.exit(1)

    # finger print verification
    def verify_fingerprint(self, body, aes_key, iv_key):
        URL = urljoin(BASE_URL(self.url), "/nibss/fp/VerifyFingerPrint")
        headers = {
            "OrganisationCode": self.code,
            "Sandbox-Key": self.key,
            "Authorization": self.auth_header,
            "SIGNATURE": self.sign_header,
            "SIGNATURE_METH": self.sign_meth,
            "Content-Type": self.content_type,
            "Accept": self.accept
        }
        encrypted = crypting.Crypt().encrypt(body, aes_key, iv_key)

        try:
            r = requests.post(url=URL, headers=headers, data=encrypted)
            if r.status_code == 200:
                data = crypting.Crypt().decrypt(r.text, aes_key, iv_key)
            elif r.status_code == 500:
                data = "server error"
            elif r.status_code == 403:
                data = "Expired Sandbox Key"
            else:
                data = "error"
            return data
        except requests.exceptions.RequestException as e:
            return e
            sys.exit(1)
