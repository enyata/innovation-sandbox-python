from urllib.parse import urljoin
from url import url as BASE_URL
from sterling.Sterling import Sterling
from sterling.utils.calls import calls


class Transfer(Sterling):
    def InterbankNameEnquiry(self, query):
        url = urljoin(BASE_URL(self.url),
                      "/sterling/TransferAPIs/api/Spay/InterbankNameEnquiry")
        header = self.headers
        apiResponse = calls("get", url, query, "", header)
        return apiResponse
