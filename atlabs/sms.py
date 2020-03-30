from atlabs.config import Atlabs
from urllib.parse import urljoin
from url import url as BASE_URL
from .utils.constants import SEND_MESSAGE, SEND_PREMIUM_MESSAGE, CREATE_PREMIUM_SUBSCRIPTION, DELETE_PREMIUM_SUBSCRIPTION, FETCH_PREMIUM_SUBSCRIPTION, FETCH_MESSAGE
from .utils.request_handler import request


class Sms(Atlabs):

    def SendMessage(self, data):
        url = urljoin(BASE_URL(self.url), SEND_MESSAGE)
        headers = self.headers
        res = request(url, data, headers)
        return (res)

    def SendPremiumMessage(self, data):
        url = urljoin(BASE_URL(self.url), SEND_PREMIUM_MESSAGE)
        headers = self.headers
        res = request(url, data, headers)
        return (res)

    def CreatePremiumSubscription(self, data):
        url = urljoin(BASE_URL(self.url), CREATE_PREMIUM_SUBSCRIPTION)
        headers = self.headers
        res = request(url, data, headers)
        return (res)

    def DeletePremiumSubscription(self, data):
        url = urljoin(BASE_URL(self.url), DELETE_PREMIUM_SUBSCRIPTION)
        headers = self.headers
        res = request(url, data, headers)
        return (res)

    def FetchPremiumSubscription(self, data):
        url = urljoin(BASE_URL(self.url), FETCH_PREMIUM_SUBSCRIPTION)
        headers = self.headers
        res = request(url, data, headers)
        return (res)

    def FetchMessage(self, data):
        url = urljoin(BASE_URL(self.url), FETCH_MESSAGE)
        headers = self.headers
        res = request(url, data, headers)
        return (res)
