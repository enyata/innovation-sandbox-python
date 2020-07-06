import json
from urllib.parse import urljoin
from url.base import url as BASE_URL
from sterling.Sterling import Sterling
from sterling.utils.calls import calls

class Billpayment(Sterling):
    def BillPaymentAdvice(self):
        url = urljoin(BASE_URL(self.url),
                      "/sterling/billpaymentapi/api/Spay/BillpaymtAdviceRequestISW")
        header = self.headers
        api_response = calls("post", url, None, "", header)
        return api_response

    def BillerPaymentItems(self, query):
        url = urljoin(BASE_URL(self.url),
                      "/sterling/billpaymentapi/api/Spay/GetBillerPmtItemsRequest")
        header = self.headers
        api_response = calls("get", url, query, "", header)
        return api_response

    def BillersISW(self, query):
        url = urljoin(BASE_URL(self.url),
                      "/sterling/billpaymentapi/api/Spay/GetBillersISWRequest")
        header = self.headers
        api_response = calls("get", url, query, "", header)
        return api_response
