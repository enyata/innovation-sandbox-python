import bcrypt
from Crypto.Cipher import AES
from hashlib import md5
from Crypto.Random import get_random_bytes
from base64 import b64encode, b64decode
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad


class Crypt:

    def __init__(self):

        self.enc_dec_method = 'utf-8'

    def encrypt(self, str_to_enc, key, iv):
        # enc_key = md5(key.encode('utf8')).digest()
        try:
            aes_obj = AES.new(key.encode(self.enc_dec_method), AES.MODE_CBC, iv.encode(self.enc_dec_method))
            hx_enc = aes_obj.encrypt(pad(str_to_enc.encode(self.enc_dec_method), 128))
            mret = b64encode(hx_enc).decode(self.enc_dec_method)

            return mret
        except ValueError as value_error:
            if value_error.args[0] == 'IV must be 16 bytes long':
                raise ValueError('Encryption Error: SALT must be 16 characters long')
            elif value_error.args[0] == 'AES key must be either 16, 24, or 32 bytes long':
                raise ValueError('Encryption Error: Encryption key must be either 16, 24, or 32 characters long')
            else:
                raise ValueError(value_error)

    def decrypt(self, enc_str, key, iv):
        try:
            raw = b64decode(enc_str)
            aes_obj = AES.new(key, AES.MODE_CBC, iv)
            mret = unpad(aes_obj.decrypt(raw), 128)
            out = mret.decode(self.enc_dec_method)
            return out
        except ValueError as value_error:
            if value_error.args[0] == 'IV must be 16 bytes long':
                raise ValueError('Decryption Error: SALT must be 16 characters long')
            elif value_error.args[0] == 'AES key must be either 16, 24, or 32 bytes long':
                raise ValueError('Decryption Error: Encryption key must be either 16, 24, or 32 characters long')
            else:
                raise ValueError(value_error)


e = Crypt().encrypt("12345678901", '9+CZaWqfyI/fwezX', "eRpKTBjdOq6T67D0")
print(e)
d = Crypt().decrypt("4C3A8O9wyPmHP76qxvjkFV7cMBIpQEwPM7PW940vRE1i9E6oVbiY1WZKVTq8n21KVNlNo6U3uHF3EyuwgwiKbNejTQlx/os7E3Wa7gsf7vpT6ZRQUpgLptDu5IO2oUUW8sSgj0DqN0ip8ngUzRqs8IC64xCShT9Zg18nO4yC4y4=", b"9+CZaWqfyI/fwezX", b"eRpKTBjdOq6T67D0" )
print(d)
