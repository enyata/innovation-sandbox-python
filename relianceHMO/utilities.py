from .utils.request_handler import request, requestWithParams
from relianceHMO.config import RelianceHMO
from urllib.parse import urljoin
from url.base import url as BASE_URL
from .utils.constants import GET_HEALTHCARE_PROVIDERS, STATE_AVAILABLE_FOR_HEALTHCARE, BENEFITS_LIST, GET_TITLES, GET_OCCUPATIONS, GET_MARITAL_STATUS


class Utilities(RelianceHMO):

    def Providers(self, payload):
        url = urljoin(BASE_URL(self.url), GET_HEALTHCARE_PROVIDERS)
        headers = self.headers
        res = requestWithParams(url, payload, headers)
        return (res)

    def States(self):
        url = urljoin(BASE_URL(self.url), STATE_AVAILABLE_FOR_HEALTHCARE)
        headers = self.headers
        res = request(url, headers)
        return (res)

    def Benefits(self, params):
        url = urljoin(BASE_URL(self.url), BENEFITS_LIST)
        headers = self.headers
        res = requestWithParams(url, params, headers)
        return (res)

    def Titles(self):
        url = urljoin(BASE_URL(self.url), GET_TITLES)
        headers = self.headers
        res = request(url, headers)
        return (res)

    def Occupations(self):
        url = urljoin(BASE_URL(self.url), GET_OCCUPATIONS)
        headers = self.headers
        res = request(url, headers)
        return (res)

    def GetMaritalStatus(self):
        url = urljoin(BASE_URL(self.url), GET_MARITAL_STATUS)
        headers = self.headers
        res = request(url, headers)
        return (res)