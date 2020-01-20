import unittest
from unittest.mock import Mock, patch
import nibss.request as RS
from nibss.tests.common import body, R

b = RS.Request({"url":"", "Organizationcode": "11111", "sandbox-key": "0ae0db703c04119b3db7a03d7f854c13", "content-type" :"application/json", "accept": "application/json", "username": "11111",
               "password": "^o'e6EXK5T ~^j2="})
class MyTestCase(unittest.TestCase):
    @patch('nibss.request.requests.post')
    def test_reset(self, mock_post):
        data = {'aes_key': '9+CZaWqfyI/fwezX', 'password': "^o'e6EXK5T ~^j2=", 'ivkey': 'eRpKTBjdOq6T67D0'}
        mock_post.return_value = R("")
        self.assertEqual(b.bvn_reset(), data, "should return an object")

    @patch('nibss.request.requests.post')
    def test_verify_single(self, mock_post):
        data = {
            'message': 'OK',
            'data': {'ResponseCode': '00', 'BVN': '12345678901', 'FirstName': 'Uchenna', 'MiddleName': 'Chijioke',
                     'LastName': 'Nwanyanwu', 'DateOfBirth': '22-Oct-1970', 'PhoneNumber': '07033333333',
                     'RegistrationDate': '16-Nov-2014', 'EnrollmentBank': '900',
                     'EnrollmentBranch': 'Victoria Island', 'WatchListed': 'NO'}}
        mock_post.return_value = R(body["single_bvn"])
        self.assertEqual(b.verify_single({"BVN": "12345678901"}, '9+CZaWqfyI/fwezX', "eRpKTBjdOq6T67D0"), data,
                         "should return object")

    @patch('nibss.request.requests.post')
    def test_multiple_bvn(self, mock_post):
        data = {
            "message": "OK", "data": {"ResponseCode": "00", "ValidationResponses": [
                {"ResponseCode": "00", "BVN": "12345678901", "FirstName": "Uchenna", "MiddleName": "Innocent",
                 "LastName": "Nwanyanwu", "DateOfBirth": "29-Oct-1995", "PhoneNumber": "07033333333",
                 "RegistrationDate": "16-Dec-2014", "EnrollmentBank": "900", "EnrollmentBranch": "Victoria Island",
                 "WatchListed": "NO"},
                {"ResponseCode": "00", "BVN": "12345678902", "FirstName": "Wale", "MiddleName": "Joshua",
                 "LastName": "Odugbemi", "DateOfBirth": "29-Oct-1996", "PhoneNumber": "07033333334",
                 "RegistrationDate": "16-Oct-2014", "EnrollmentBank": "900",
                 "EnrollmentBranch": "No. 2 NIBSS Avenue, VI",
                 "WatchListed": "YES"},
                {"ResponseCode": "00", "BVN": "12345678903", "FirstName": "Seun", "MiddleName": "Ogunjimi",
                 "LastName": "Isaiah", "DateOfBirth": "29-Oct-1997", "PhoneNumber": "07033333336",
                 "RegistrationDate": "16-Sept-2014", "EnrollmentBank": "900", "EnrollmentBranch": "Ikorodu",
                 "WatchListed": "NO"}]}}
        mock_post.return_value = R(body["multiple_bvn"])
        self.assertEqual(b.verify_multiple({"BVNS": "12345678901, 12345678902, 12345678903"}, "9+CZaWqfyI/fwezX",
                                           "eRpKTBjdOq6T67D0"), data,
                         "should return object")

    @patch('nibss.request.requests.post')
    def test_watchlisted(self, mock_post):
        output = {
            "message": "OK",
            "data": {
                "ResponseCode": "00",
                "BVN": "12345678901",
                "BankCode": "900",
                "Category": "1",
                "WatchListed": "YES"
            }
        }
        mock_post.return_value = R(body["watchlist"])
        self.assertEqual(b.bvn_watchlisted({"BVN": "12345678901"}, '9+CZaWqfyI/fwezX', "eRpKTBjdOq6T67D0"), output,
                         "should return an object")

    @patch('nibss.request.requests.post')
    def test_placeholder_reset(self, mock_post):
        data = {'aes_key': '9+CZaWqfyI/fwezX', 'password': "^o'e6EXK5T ~^j2=", 'ivkey': 'eRpKTBjdOq6T67D0'}
        mock_post.return_value = R("")
        self.assertEqual(b.bvn_placeholder_reset(), data, "should return an object")

    @patch('nibss.request.requests.post')
    def test_validate_record(self, mock_post):
        response = {
            "message": "OK",
            "data": {
                "ResponseCode": "00",
                "BVN": "VALID",
                "FirstName": "VALID",
                "LastName": "VALID",
                "MiddleName": "INVALID",
                "AccountNumber": "VALID",
                "BankCode": "VALID"
            }
        }
        mock_post.return_value = R(body["record"])
        self.assertEqual(b.validate_record({
            "BVN": "12345678901",
            "FirstName": "Uchenna",
            "LastName": "Okoro",
            "MiddleName": "Adepoju",
            "AccountNumber": "0987654321",
            "BankCode": "011"
        }, '9+CZaWqfyI/fwezX', "eRpKTBjdOq6T67D0"), response, "should return an object")

    @patch('nibss.request.requests.post')
    def test_validate_records(self, mock_post):
        response = {
            'message': 'OK',
            'data': {'ValidationResponses': [
                {
                    'ResponseCode': '00',
                    'BVN': 'VALID',
                    'FirstName': 'VALID',
                    'LastName': 'VALID',
                    'MiddleName': 'INVALID',
                    'AccountNumber': 'VALID',
                    'BankCode': 'VALID'},
                {
                    'ResponseCode': '00', 'BVN': 'VALID', 'FirstName': 'INVALID', 'LastName': 'VALID', 'MiddleName': 'INVALID', 'AccountNumber': 'VALID', 'BankCode': 'VALID'
                }]}}
        mock_post.return_value = R(body["records"])
        self.assertEqual(b.validate_records([
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
    ], "9+CZaWqfyI/fwezX", "eRpKTBjdOq6T67D0"), response, "should return an object")

    @patch('nibss.request.requests.post')
    def test_verify_finger_print(self, mock_post):
        response = {
            "message": "OK",
            "data": {
                "BVN": "12345678901",
                "ResponseCode": "00"
            }
        }
        mock_post.return_value = R(body["fingerprint_data"])
        self.assertEqual(b.verify_fingerprint({
            "BVN": "12345678901",
            "DeviceId": "Z000112BC12",
            "ReferenceNumber": "00099201710012205354422",
            "FingerImage": {
                "type": "ISO_2005",
                "position": "RT",
                "nist_impression_type": "0",
                "value": "c2RzZnNkZnNzZGY="
            }
        }, '9+CZaWqfyI/fwezX', "eRpKTBjdOq6T67D0"), response, "should return an object")



if __name__ == '__main__':
    unittest.main()
