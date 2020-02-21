from nibss.Nibss import Nibss
from urllib.parse import urljoin
from nibss.utils.calls import request, encrypted_request
from url import url as BASE_URL


class Record(Nibss):
    def bvn_placeholder_reset(self):
        headers = self.header
        URL = urljoin(BASE_URL(self.url), "/nibss/BVNPlaceHolder/Reset")
        return request(headers, URL)

    def validate_record(self, data):
        URL = urljoin(BASE_URL(self.url), "/nibss/BVNPlaceHolder/ValidateRecord")
        headers = self.headers
        body = data["body"]
        return encrypted_request(headers, URL, data["Aes_key"], data["Iv_key"], body)

    def validate_records(self, data):
        URL = urljoin(BASE_URL(self.url), "/nibss/BVNPlaceHolder/ValidateRecords")
        headers = self.headers
        body = data["body"]
        return encrypted_request(headers, URL, data["Aes_key"], data["Iv_key"], body)


