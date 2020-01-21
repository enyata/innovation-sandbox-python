import unittest
from unittest.mock import Mock, patch

from Crypto.Random import random

import nibss.request as RS
from nibss.tests.common import body, R, iv, aes, responses

b = RS.Request({"base_url": "", "Organizationcode": "11111", "sandbox-key": "0ae0db703c04119b3db7a03d7f854c13",
                "content-type": "application/json", "accept": "application/json", "username": "11111",
                "password": "^o'e6EXK5T ~^j2="})


class MyTestCase(unittest.TestCase):
    @patch('nibss.request.requests.post')
    def test_reset(self, mock_post):
        data = {'aes_key': '9+CZaWqfyI/fwezX', 'password': "^o'e6EXK5T ~^j2=", 'ivkey': 'eRpKTBjdOq6T67D0'}
        mock_post.return_value = R("")
        self.assertEqual(b.sandbox_reset(),
                         data,
                         "should return an object")

    @patch('nibss.request.requests.post')
    def test_verify_single(self, mock_post):
        data = responses["single_bvn"]
        mock_post.return_value = R(body["single_bvn"])
        self.assertEqual(b.verify_single({"body":{"BVN": "12345678901"}, "Aes_key":aes, "Iv_key":iv}),
                         data,
                         "should return object")

    @patch('nibss.request.requests.post')
    def test_multiple_bvn(self, mock_post):
        data = responses["multiple_bvn"]
        mock_post.return_value = R(body["multiple_bvn"])
        self.assertEqual(b.verify_multiple({"bvns":{"BVNS": "1234567890 1, 12345678902, 12345678903"}, "Aes_key":aes, "Iv_key":iv}),
                         data,
                         "should return object")

    @patch('nibss.request.requests.post')
    def test_watchlisted(self, mock_post):
        output = responses["watchlist"]
        mock_post.return_value = R(body["watchlist"])
        self.assertEqual(b.bvn_watchlisted({"body":{"BVN": "12345678901"}, "Aes_key":aes, "Iv_key":iv}),
                         output,
                         "should return an object")

    @patch('nibss.request.requests.post')
    def test_placeholder_reset(self, mock_post):
        data = {'aes_key': '9+CZaWqfyI/fwezX', 'password': "^o'e6EXK5T ~^j2=", 'ivkey': 'eRpKTBjdOq6T67D0'}
        mock_post.return_value = R("")
        self.assertEqual(b.bvn_placeholder_reset(),
                         data,
                         "should return an object")

    @patch('nibss.request.requests.post')
    def test_validate_record(self, mock_post):
        response = responses["record"]
        mock_post.return_value = R(body["record"])
        self.assertEqual(b.validate_record({"body":{
            "BVN": "12345678901",
            "FirstName": "Uchenna",
            "LastName": "Okoro",
            "MiddleName": "Adepoju",
            "AccountNumber": "0987654321",
            "BankCode": "011"
        }, "Aes_key":aes, "Iv_key":iv}),
            response,
            "should return an object")

    @patch('nibss.request.requests.post')
    def test_validate_records(self, mock_post):
        response = responses["records"]
        mock_post.return_value = R(body["records"])
        self.assertEqual(b.validate_records({"body":[
            {
                "BVN": "12345678901",
                "FirstName": "Uchenna",
                "LastName": "Okoro",
                "MiddleName": "Adepoju",
                "AccountNumber": "0987654321",
                "BankCode": "011"
            },
            {
                "BVN": "12345678912",
                "FirstName": "Chidi",
                "LastName": "Seun",
                "MiddleName": "Joshua",
                "AccountNumber": "0987654329",
                "BankCode": "012"
            }
        ], "Aes_key":aes, "Iv_key":iv}), response, "should return an object")

    @patch('nibss.request.requests.post')
    def test_verify_finger_print(self, mock_post):
        response = responses["fingerprint_data"]
        mock_post.return_value = R(body["fingerprint_data"])
        self.assertEqual(b.verify_fingerprint({"body":{
            "BVN": "12345678901",
            "DeviceId": "Z000112BC12",
            "ReferenceNumber": "00099201710012205354422",
            "FingerImage": {
                "type": "ISO_2005",
                "position": "RT",
                "nist_impression_type": "0",
                "value": "c2RzZnNkZnNzZGY="
            }
        }, "Aes_key":aes, "Iv_key":iv}), response, "should return an object")


if __name__ == '__main__':
    unittest.main()