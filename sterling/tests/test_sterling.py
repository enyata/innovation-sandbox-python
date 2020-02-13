import unittest
from requests import Session
from unittest.mock import Mock, patch
from sterling.tests.common import responses, body, query, R
from sterling.name_enquiry import Enquiry
from sterling.transfer import Transfer

header = {
    "base_url": "",
    "Sandbox-Key": "0ae0db703c04119b3db7a03d7f854c13",
    "Ocp-Apim-Subscription-Key": "t",
    "Ocp-Apim-Trace": "true",
    "Appid": "69",
    "Content-Type": "application/json",
    "ipval": "0"
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
