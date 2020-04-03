from .utils.calls import encrypted_request, request
from nibss.Nibss import Nibss
from urllib.parse import urljoin
from url import url as BASE_URL


class FingerPrint(Nibss):
    def verify_fingerprint(self, data):
        URL = urljoin(BASE_URL(self.url), "/nibss/fp/VerifyFingerPrint")
        headers = self.headers
        body = data["body"]
        return encrypted_request(headers, URL, data["Aes_key"], data["Iv_key"], body)

    def reset(self):
        headers = self.header
        URL = urljoin(BASE_URL(self.url), "/nibss/fp/Reset")
        return request(headers, URL)