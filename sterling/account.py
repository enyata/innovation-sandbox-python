import json
from urllib.parse import urljoin
from url.base import url as BASE_URL
from sterling.Sterling import Sterling
from sterling.utils.calls import calls


class Account(Sterling):
    def InterbankTransferReq(self, body):
        url = urljoin(BASE_URL(self.url),
                      "/sterling/accountapi/api/Spay/InterbankTransferReq")
        header = self.headers
        api_response = calls("post", url, None, json.dumps(body), header)
        return (api_response)
    
    def MobileWalletRequest(self, body):
        url = urljoin(BASE_URL(self.url),
                      "/sterling/accountapi/api/Spay/SBPMWalletRequest"
                      )
        header = self.headers
        api_response = calls("post", url, None, json.dumps(body), header)
        return (api_response)