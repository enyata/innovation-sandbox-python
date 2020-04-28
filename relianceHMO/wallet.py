from relianceHMO.config import RelianceHMO
from urllib.parse import urljoin
from url.base import url as BASE_URL
from .utils.constants import WALLET_BALANCE, FUND_WALLET, PARTNERSHIP_WALLET_TRANSACTION
from .utils.request_handler import request, requestWithBody


class Wallet(RelianceHMO):

    def WalletBalance(self):
        url = urljoin(BASE_URL(self.url), WALLET_BALANCE)
        headers = self.headers
        res = request(url, headers)
        return (res)

    def FundWallet(self, body):
        url = urljoin(BASE_URL(self.url), FUND_WALLET)
        headers = self.headers
        res = requestWithBody(url, body, headers)
        return (res)

    def PartnershipWalletTransactions(self):
        url = urljoin(BASE_URL(self.url), PARTNERSHIP_WALLET_TRANSACTION)
        headers = self.headers
        res = request(url, headers)
        return (res)