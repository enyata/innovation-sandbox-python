from nibss.Nibss import Nibss
from urllib.parse import urljoin
from url import url as BASE_URL
from nibss.utils.calls import request


class Credentials(Nibss):
    def reset(self):
        headers = self.header
        URL = urljoin(BASE_URL(self.url), "/nibss/bvnr/Reset")
        return request(headers, URL)
