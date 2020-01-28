import datetime
import hashlib
from nibss.utils import crypt as crypting


class Nibss:
    def __init__(self, params):
        self.url = params["base_url"]
        self.key = params["sandbox-key"]
        self.content_type = params["content-type"]
        self.accept = params["accept"]
        self.code = crypting.Crypt().hash(params["Organizationcode"])
        self.sign_meth = 'SHA256'
        auth_string = params["username"] + ':' + params["password"]
        self.auth_header = crypting.Crypt().hash(auth_string)
        datenow = str(datetime.date.today()).split('-')
        date = ''.join(datenow)
        signature_string = params["username"] + str(date) + params["password"]
        self.sign_header = hashlib.sha256(signature_string.encode('utf-8')).hexdigest()

        self.headers = {
            "OrganisationCode": self.code,
            "Sandbox-Key": self.key,
            "Authorization": self.auth_header,
            "SIGNATURE": self.sign_header,
            "SIGNATURE_METH": self.sign_meth,
            "Content-Type": self.content_type,
            "Accept": self.accept
        }
        self.header = {
            "OrganisationCode": self.code,
            "Sandbox-Key": self.key
        }