from atlabs.config import Atlabs
from urllib.parse import urljoin
from url import url as BASE_URL
from .utils.constants import CREATE_CHECKOUT_TOKEN
from .utils.request_handler import request


class Token(Atlabs):

    def CreateCheckoutToken(self, data):
        url = urljoin(BASE_URL(self.url), CREATE_CHECKOUT_TOKEN)
        headers = self.headers
        res = request(url, data, headers)
        return (res)
