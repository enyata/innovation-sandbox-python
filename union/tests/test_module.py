import unittest
from unittest.mock import Mock, patch
from .common import header, body, params, responses, R
from union.token import Token
from union.enquiry import Enquiry
from union.user import User


@patch('requests.post')
def test_access_token_generator(mock_post):
    data = responses['AccessTokenGenerator']
    mock_post.return_value = R(data)
    header['Content-Type'] = 'application/x-www-form-urlencoded'
    assert Token(header).AccessTokenGenerator(
        body["AccessTokenGenerator"]) == data, "should return an object"


@patch('requests.post')
def test_account_enquiry(mock_post):
    data = responses['AccountEnquiry']
    mock_post.return_value = R(data)
    assert Enquiry(header).Account(
        body["AccountEnquiry"], params['access_token']) == data, "should return an object"


@patch('requests.post')
def test_customer_enquiry(mock_post):
    data = responses['CustomerEnquiry']
    mock_post.return_value = R(data)
    assert Enquiry(header).Customer(
        body["CustomerEnquiry"], params['access_token']) == data, "should return an object"

@patch('requests.post')
def test_customer_and_account_enquiry(mock_post):
    data = responses['CustomerAndAccountEnquiry']
    mock_post.return_value = R(data)
    assert Enquiry(header).CustomerAndAccount(
        body["CustomerAndAccountEnquiry"], params['access_token']) == data, "should return an object"


@patch('requests.post')
def test_change_user_credentials(mock_post):
    data = responses['ChangeUserCredentials']
    mock_post.return_value = R(data)
    assert User(header).ChangeUsersCredentials(
        body["ChangeUserCredentials"], params['access_token']) == data, "should return an object"
