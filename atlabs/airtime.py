from atlabs.config import Atlabs
from urllib.parse import urljoin
from url import url as BASE_URL
from .utils.constants import SEND_AIRTIME
from .utils.request_handler import request


class Airtime(Atlabs):

    def SendAirtime(self, data):
        url = urljoin(BASE_URL(self.url), SEND_AIRTIME)
        headers = self.headers
        res = request(url, data, headers)
        return (res)
