from relianceHMO.config import RelianceHMO
from urllib.parse import urljoin
from url.base import url as BASE_URL
from .utils.constants import GET_ALL_PLANS
from .utils.request_handler import requestWithParams, requestWithBody


class Plans(RelianceHMO):

    def GetAllPlans(self, params):
        url = urljoin(BASE_URL(self.url), GET_ALL_PLANS)
        headers = self.headers
        res = requestWithParams(url, params, headers)
        return (res)