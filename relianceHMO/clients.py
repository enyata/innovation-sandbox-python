from relianceHMO.config import RelianceHMO
from urllib.parse import urljoin
from url.base import url as BASE_URL
from .utils.constants import SIGNUP_COMPANY, RENEW_SUBSCRIPTION_COMPANY
from .utils.request_handler import requestWithBody, requestWithPut


class Clients(RelianceHMO):

    def SignupCompany(self, payload):
        url = urljoin(BASE_URL(self.url), SIGNUP_COMPANY)
        headers = self.headers
        res = requestWithBody(url, payload, headers)
        return (res)

    def  RenewSubscriptionCompany(self, payload):
        url = urljoin(BASE_URL(self.url), RENEW_SUBSCRIPTION_COMPANY)
        headers = self.headers
        res = requestWithPut(url, payload, headers)
        return (res)
