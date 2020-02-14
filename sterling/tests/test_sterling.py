import unittest
from requests import Session
from unittest.mock import Mock, patch
from sterling.tests.common import responses, body, query, R
from sterling.name_enquiry import Enquiry
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

@patch.object(Session, 'request')
def test_enquiry(mock_get):
    data = responses["enquiry"]
    mock_get.return_value = R(responses["enquiry"])
    assert Enquiry(header).name_enquiry(query) == data, "should return an object"


@patch.object(Session, 'request')
def test_transfer(mock_post):
    data = responses["transfer"]
    mock_post.return_value = R(responses["transfer"])
    assert Transfer(header).transfer(body) == data, "should return an object"
