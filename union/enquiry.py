from union.config import Union
from urllib.parse import urljoin
from url import url as BASE_URL
from .utils.constants import ACCOUNT_ENQUIRY, CUSTOMER_ENQUIRY, CUSTOMER_AND_ACCOUNT_ENQUIRY
from .utils.request_handler import requestWithParams


class Enquiry(Union):

    def Account(self, body, params):
        url = urljoin(BASE_URL(self.url), ACCOUNT_ENQUIRY)
        headers = self.headers
        res = requestWithParams(url, body, params, headers)
        return (res)

    def Customer(self, body, params):
        url = urljoin(BASE_URL(self.url), CUSTOMER_ENQUIRY)
        headers = self.headers
        res = requestWithParams(url, body, params, headers)
        return (res)

    def CustomerAndAccount(self, body, params):
        url = urljoin(BASE_URL(self.url), CUSTOMER_AND_ACCOUNT_ENQUIRY)
        headers = self.headers
        res = requestWithParams(url, body, params, headers)
        return (res)
