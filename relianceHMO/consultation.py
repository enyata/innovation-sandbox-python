from relianceHMO.config import RelianceHMO
from urllib.parse import urljoin
from url.base import url as BASE_URL
from .utils.constants import REQUEST_CONSULTATION
from .utils.request_handler import requestWithBodyAndParams


class Consultation(RelianceHMO):

    def RequestConsultation(self, params):
        url = urljoin(BASE_URL(self.url), REQUEST_CONSULTATION)
        headers = self.headers
        body = {}
        res = requestWithBodyAndParams(url, body, params, headers)
        return (res)
