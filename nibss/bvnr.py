from nibss.utils.calls import encrypted_request, request
from nibss.Nibss import Nibss
from urllib.parse import urljoin
from url import url as BASE_URL


class Bvn(Nibss):
    def verify_single(self, data):
        URL = urljoin(BASE_URL(self.url), "/nibss/bvnr/VerifySingleBVN")
        headers = self.headers
        body = data["body"]
        return encrypted_request(headers, URL, data["Aes_key"], data["Iv_key"], body)

    def verify_multiple(self, data):
        URL = urljoin(BASE_URL(self.url), "/nibss/bvnr/VerifyMultipleBVN")
        headers = self.headers
        body = data["bvns"]
        return encrypted_request(headers, URL, data["Aes_key"], data["Iv_key"], body)

    def bvn_watchlisted(self, data):
        URL = urljoin(BASE_URL(self.url), "/nibss/bvnr/IsBVNWatchlisted")
        headers = self.headers
        body = data["body"]
        return encrypted_request(headers, URL, data["Aes_key"], data["Iv_key"], body)

    def get_single(self, data):
        URL = urljoin(BASE_URL(self.url), "/nibss/bvnr/GetSingleBVN")
        headers = self.headers
        body = data["body"]
        return encrypted_request(headers, URL, data["Aes_key"], data["Iv_key"], body)

    def get_multiple(self, data):
        URL = urljoin(BASE_URL(self.url), "/nibss/bvnr/GetMultipleBVN")
        headers = self.headers
        body = data["bvns"]
        return encrypted_request(headers, URL, data["Aes_key"], data["Iv_key"], body)

    def reset(self):
        headers = self.header
        URL = urljoin(BASE_URL(self.url), "/nibss/bvnr/Reset")
        return request(headers, URL)