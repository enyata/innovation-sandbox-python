from relianceHMO.config import RelianceHMO
from urllib.parse import urljoin
from url.base import url as BASE_URL
from .utils.constants import GET_ALL_ENROLLEE, REGISTER_ENROLLEE_INDIVIDUALS, ENROLLEES_ID_CARD, COMPLETE_ENROLLEE_PROFILE, ENROLLEES_VALIDATION
from .utils.request_handler import  requestWithParams, requestWithBody, requestWithPutAndParams


class Enrollees(RelianceHMO):

    def Register(self, payload):
        url = urljoin(BASE_URL(self.url), REGISTER_ENROLLEE_INDIVIDUALS)
        headers = self.headers
        res = requestWithBody(url, payload, headers)
        return (res)

    def GetAllEnrollee(self, params):
        url = urljoin(BASE_URL(self.url), GET_ALL_ENROLLEE)
        headers = self.headers
        res = requestWithParams(url, params, headers)
        return (res)

    def GetEnrollee(self, params):
        url = urljoin(BASE_URL(self.url), ENROLLEES_ID_CARD)
        headers = self.headers
        res = requestWithParams(url, params, headers)
        return (res)

    def Profile(self, params):
        url = urljoin(BASE_URL(self.url), COMPLETE_ENROLLEE_PROFILE)
        headers = self.headers
        body = "{}"
        res = requestWithPutAndParams(url, params, body, headers)
        return (res)

    def Validate(self, params):
        url = urljoin(BASE_URL(self.url), ENROLLEES_VALIDATION)
        headers = self.headers
        res = requestWithParams(url, params, headers)
        return (res)

    def Card(self, params):
        url = urljoin(BASE_URL(self.url), ENROLLEES_ID_CARD)
        headers = self.headers
        res = requestWithParams(url, params, headers)
        return (res)