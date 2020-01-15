from Crypto.Cipher import AES
from base64 import b64encode, b64decode
from Crypto.Util.Padding import pad, unpad
import binascii
import json


class Crypt:

    def __init__(self):
        self.enc_dec_method = 'utf-8'

    def encrypt(self, str_to_enc, key, iv):
        try:
            aes_obj = AES.new(key.encode(self.enc_dec_method), AES.MODE_CBC, iv.encode(self.enc_dec_method))
            text= json.dumps(str_to_enc)
            hx_enc = aes_obj.encrypt(pad(text.encode(self.enc_dec_method), 16))
            mret = binascii.hexlify(hx_enc).decode(self.enc_dec_method)
            return mret

        except ValueError as value_error:
            if value_error.args[0] == 'IV must be 16 bytes long':
                raise ValueError('Encryption Error: IV key must be 16 characters long')
            elif value_error.args[0] == 'AES key must be either 16, 24, or 32 bytes long':
                raise ValueError('Encryption Error: Encryption key must be either 16, 24, or 32 characters long')
            else:
                raise ValueError(value_error)

    def decrypt(self, enc_str, key, iv):
        try:
            raw = binascii.unhexlify(enc_str)
            aes_obj = AES.new(key.encode(self.enc_dec_method), AES.MODE_CBC, iv.encode(self.enc_dec_method))
            mret = unpad(aes_obj.decrypt(raw), 16)
            out = mret.decode(self.enc_dec_method)
            return json.loads(out)

        except ValueError as value_error:
            if value_error.args[0] == 'IV must be 16 bytes long':
                raise ValueError('Decryption Error: IV key must be 16 characters long')
            elif value_error.args[0] == 'AES key must be either 16, 24, or 32 bytes long':
                raise ValueError('Decryption Error: Encryption key must be either 16, 24, or 32 characters long')
            else:
                raise ValueError(value_error)


