from union.config import Union
from urllib.parse import urljoin
from url import url as BASE_URL
from .utils.constants import CHANGE_USERS_CREDENTIALS
from .utils.request_handler import requestWithParams


class User(Union):

    def ChangeUsersCredentials(self, body, params):
        url = urljoin(BASE_URL(self.url), CHANGE_USERS_CREDENTIALS)
        headers = self.headers
        res = requestWithParams(url, body, params, headers)
        return (res)
