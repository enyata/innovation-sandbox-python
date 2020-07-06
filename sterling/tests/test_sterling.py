import unittest
from requests import Session
from unittest.mock import Mock, patch
from sterling.billpayment import Billpayment
from sterling.tests.common import responses, body, query,mobile_wallet_transfer_body, get_biller_query, R
from sterling.account import Account
from sterling.transfer import Transfer
from faker import Faker

fake = Faker().random_number()

header = {
    "base_url": "",
    "Sandbox-Key": str(Faker().text()),
    "Ocp-Apim-Subscription-Key": str(Faker().text()),
    "Ocp-Apim-Trace": "true",
    "Appid": str(fake),
    "Content-Type": "application/json",
    "ipval": str(fake)
}

biller = {
    "Ocp-Apim-Subscription-Key": str(Faker().text())
}

@patch.object(Session, 'request')
def test_enquiry(mock_get):
    data = responses["enquiry"]
    mock_get.return_value = R(responses["enquiry"])
    assert Transfer(header).InterbankNameEnquiry(query) == data, "should return an object"

@patch.object(Session, 'request')
def test_transfer(mock_post):
    data = responses["transfer"]
    mock_post.return_value = R(responses["transfer"])
    assert Account(header).InterbankTransferReq(body) == data, "should return an object"

@patch.object(Session, 'request')
def test_mobile_wallet_transfer(mock_post):
    data = responses["mobile_wallet_transfer"]
    mock_post.return_value = R(data)
    assert Account(header).MobileWalletRequest(mobile_wallet_transfer_body) == data, "should return an object"

@patch.object(Session, 'request')
def test_bill_payment_advice(mock_post):
    data = responses["bill_payment_advice"]
    mock_post.return_value = R(data)
    assert Billpayment(header).BillPaymentAdvice() == data, "should return an object"

@patch.object(Session, 'request')
def test_biller_payment_items(mock_get):
    data = responses["biller_payment_items"]
    mock_get.return_value = R(data)
    assert Billpayment(biller).BillerPaymentItems(get_biller_query) == data, "should return an object"

@patch.object(Session, 'request')
def test_biller_isw(mock_get):
    data = responses["test_biller_isw"]
    mock_get.return_value = R(data)
    assert Billpayment(biller).BillersISW(get_biller_query) == data, "should return an object"
