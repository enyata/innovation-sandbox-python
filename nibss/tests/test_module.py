import pytest
from unittest.mock import Mock, patch
from nibss.bvnr import Bvn
from nibss.records import Record
from nibss.fingerprint import FingerPrint
from nibss.tests.common import body, R, iv, aes, responses

b = {
    "base_url": "", "Organizationcode": "11111", "sandbox-key": "0hsagshfkdasjhkgfsdhlkjhgsvhgikjs",
    "content-type": "application/json", "accept": "application/json", "username": "11111", "password": "nbvhjfihkjsd"
}


@patch('requests.post')
def test_bvn_reset(mock_post):
    data = {'aes_key': aes, 'password': "fdgfudkjd", 'ivkey': iv}
    mock_post.return_value = R("")
    assert Bvn(b).reset() == data, "should return an object"


@patch('requests.post')
def test_fp_reset(mock_post):
    data = {'aes_key': aes, 'password': "fdgfudkjd", 'ivkey': iv}
    mock_post.return_value = R("")
    assert FingerPrint(b).reset() == data, "should return an object"


@patch('requests.post')
def test_verify_single(mock_post):
    data = responses["single_bvn"]
    mock_post.return_value = R(body["single_bvn"])
    assert Bvn(b).verify_single({"body": {"BVN": "12345678901"},
                                 "Aes_key": aes, "Iv_key": iv}) == data, "should return object"


@patch('requests.post')
def test_multiple_bvn(mock_post):
    data = responses["multiple_bvn"]
    mock_post.return_value = R(body["multiple_bvn"])
    assert Bvn(b).verify_multiple({"bvns": {"BVNS": "1234567890 1, 12345678902, 12345678903"},
                                   "Aes_key": aes, "Iv_key": iv}) == data, "should return object"


@patch('requests.post')
def test_get_single(mock_post):
    data = responses["single_bvn"]
    mock_post.return_value = R(body["single_bvn"])
    assert Bvn(b).verify_single({"body": {"BVN": "12345678901"},
                                 "Aes_key": aes, "Iv_key": iv}) == data, "should return object"


@patch('requests.post')
def test_get_multiple_bvn(mock_post):
    data = responses["multiple_bvn"]
    mock_post.return_value = R(body["multiple_bvn"])
    assert Bvn(b).verify_multiple({"bvns": {"BVNS": "1234567890 1, 12345678902, 12345678903"},
                                   "Aes_key": aes, "Iv_key": iv}) == data, "should return object"


@patch('requests.post')
def test_watchlisted(mock_post):
    output = responses["watchlist"]
    mock_post.return_value = R(body["watchlist"])
    assert Bvn(b).bvn_watchlisted({"body": {
        "BVN": "12345678901"}, "Aes_key": aes, "Iv_key": iv}) == output, "should return an object"


@patch('requests.post')
def test_placeholder_reset(mock_post):
    data = {'aes_key': aes, 'password': "fdgfudkjd", 'ivkey': iv}
    mock_post.return_value = R("")
    assert Record(b).bvn_placeholder_reset() == data, "should return an object"


@patch('requests.post')
def test_validate_record(mock_post):
    response = responses["record"]
    mock_post.return_value = R(body["record"])
    assert Record(b).validate_record({
        "body": {
            "BVN": "12345678901",
            "FirstName": "Uchenna",
            "LastName": "Okoro",
            "MiddleName": "Adepoju",
            "AccountNumber": "0987654321",
            "BankCode": "011"
        },
        "Aes_key": aes, "Iv_key": iv}) == response, "should return an object"


@patch('requests.post')
def test_validate_records(mock_post):
    response = responses["records"]
    mock_post.return_value = R(body["records"])
    assert Record(b).validate_records({"body": [
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
    ], "Aes_key": aes, "Iv_key": iv}) == response, "should return an object"


@patch('requests.post')
def test_verify_finger_print(mock_post):
    response = responses["fingerprint_data"]
    mock_post.return_value = R(body["fingerprint_data"])
    assert FingerPrint(b).verify_fingerprint({"body": {
        "BVN": "12345678901",
        "DeviceId": "Z000112BC12",
        "ReferenceNumber": "00099201710012205354422",
        "FingerImage": {
            "type": "ISO_2005",
            "position": "RT",
            "nist_impression_type": "0",
            "value": "c2RzZnNkZnNzZGY="
        }
    }, "Aes_key": aes, "Iv_key": iv}) == response, "should return an object"
