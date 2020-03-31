from atlabs.config import Atlabs
from urllib.parse import urljoin
from url import url as BASE_URL
from .utils.constants import VOICE_CALL, QUEUE_STATUS, MEDIA_UPLOAD
from .utils.request_handler import request


class Voice(Atlabs):

    def VoiceCall(self, data):
        url = urljoin(BASE_URL(self.url), VOICE_CALL)
        headers = self.headers
        res = request(url, data, headers)
        return (res)

    def QueueStatus(self, data):
        url = urljoin(BASE_URL(self.url), QUEUE_STATUS)
        headers = self.headers
        res = request(url, data, headers)
        return (res)

    def MediaUpload(self, data):
        url = urljoin(BASE_URL(self.url), MEDIA_UPLOAD)
        headers = self.headers
        res = request(url, data, headers)
        return (res)
