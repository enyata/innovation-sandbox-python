from union.config import Union
from urllib.parse import urljoin
from url import url as BASE_URL
from .utils.constants import ACCESS_TOKEN_GENERATOR
from .utils.request_handler import request


class Token(Union):

    def AccessTokenGenerator(self, data):
        url = urljoin(BASE_URL(self.url), ACCESS_TOKEN_GENERATOR)
        headers = self.headers
        res = request(url, data, headers)
        return (res)
