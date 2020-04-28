from relianceHMO.config import RelianceHMO
from urllib.parse import urljoin
from url.base import url as BASE_URL
from .utils.constants import SIGNUP_INDIVIDUALS, RENEW_SUBSCRIPTION_INDIVIDUALS
from .utils.request_handler import requestWithBody, requestWithPut


class Retails(RelianceHMO):

    def SignupIndividuals(self, body):
        url = urljoin(BASE_URL(self.url), SIGNUP_INDIVIDUALS)
        headers = self.headers
        res = requestWithBody(url, body, headers)
        return (res)

    def Renew(self, body):
        url = urljoin(BASE_URL(self.url), RENEW_SUBSCRIPTION_INDIVIDUALS)
        headers = self.headers
        res = requestWithPut(url, body, headers)
        return (res)
