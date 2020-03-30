import json
from urllib.parse import urljoin
from url import url as BASE_URL
from sterling.Sterling import Sterling
from sterling.utils.calls import calls


class Account(Sterling):
    def InterbankTransferReq(self, body):
        url = urljoin(BASE_URL(self.url),
                      "/sterling/accountapi/api/Spay/InterbankTransferReq")
        header = self.headers
        apiResponse = calls("post", url, None, json.dumps(body), header)
        return (apiResponse)
