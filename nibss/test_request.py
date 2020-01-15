import unittest

import jsonify as jsonify
import json

import nibss.request as RS

b = RS.Request({"Organizationcode": "11111", "sandbox-key": "8dc1337c1ac82aa90f3bd7b8de8d882a", "content-type" :"application/json", "accept": "application/json", "username": "11111",
               "password": "^o'e6EXK5T ~^j2="})


class MyTestCase(unittest.TestCase):
    def test_get_params(self):
        data = {"Organizationcode": "11111", "sandbox-key": "8dc1337c1ac82aa90f3bd7b8de8d882a", "content-type" :"application/json", "accept": "application/json", "username": "11111",
               "password": "^o'e6EXK5T ~^j2="}
        self.assertEqual(b.get_params(), data, "should return a dictionary")

    def test_reset(self):
        data = {'aes_key': '9+CZaWqfyI/fwezX', 'password': "^o'e6EXK5T ~^j2=", 'ivkey': 'eRpKTBjdOq6T67D0'}
        self.assertEqual(b.bvn_reset(), data, "should return an object")

    def test_single_bvn(self):
        data = {
            'message': 'OK',
            'data': {'ResponseCode': '00', 'BVN': '12345678901', 'FirstName': 'Uchenna', 'MiddleName': 'Chijioke',
                     'LastName': 'Nwanyanwu', 'DateOfBirth': '22-Oct-1970', 'PhoneNumber': '07033333333',
                     'RegistrationDate': '16-Nov-2014', 'EnrollmentBank': '900',
                     'EnrollmentBranch': 'Victoria Island', 'WatchListed': 'NO'}}
        self.assertEqual(b.verify_single({"BVN": "12345678901"}, '9+CZaWqfyI/fwezX', "eRpKTBjdOq6T67D0"), data,
                         "should return object")

    def test_multiple_bvn(self):
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
        self.assertEqual(b.verify_multiple({"BVNS": "12345678901, 12345678902, 12345678903"}, "9+CZaWqfyI/fwezX",
                                           "eRpKTBjdOq6T67D0"), data,
                         "should return object")

    def test_watchlisted(self):
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
        self.assertEqual(b.bvn_watchlisted({"BVN": "12345678901"}, '9+CZaWqfyI/fwezX', "eRpKTBjdOq6T67D0"), output,
                         "should return an object")

    def test_placeholder_reset(self):
        data = {'aes_key': '9+CZaWqfyI/fwezX', 'password': "^o'e6EXK5T ~^j2=", 'ivkey': 'eRpKTBjdOq6T67D0'}
        self.assertEqual(b.bvn_placeholder_reset(), data, "should return an object")

    def test_validate_record(self):
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
        self.assertEqual(b.validate_record({
            "BVN": "12345678901",
            "FirstName": "Uchenna",
            "LastName": "Okoro",
            "MiddleName": "Adepoju",
            "AccountNumber": "0987654321",
            "BankCode": "011"
        }, '9+CZaWqfyI/fwezX', "eRpKTBjdOq6T67D0"), response, "should return an object")

    def test_validate_records(self):
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

    def test_verify_finger_print(self):
        response = {
            "message": "OK",
            "data": {
                "BVN": "12345678901",
                "ResponseCode": "00"
            }
        }

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
