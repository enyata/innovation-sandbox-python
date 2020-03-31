import unittest
from unittest.mock import Mock, patch
from .common import header, body, responses, R
from atlabs.sms import Sms
from atlabs.token import Token
from atlabs.voice import Voice
from atlabs.airtime import Airtime


@patch('requests.post')
def test_create_checkout_token(mock_post):
    data = responses['CreateCheckoutToken']
    mock_post.return_value = R(data)
    assert Token(header).CreateCheckoutToken(
        body["CreateCheckoutToken"]) == data, "should return an object"


@patch('requests.post')
def test_create_premium_subscription(mock_post):
    data = responses['CreatePremiumSubscription']
    mock_post.return_value = R(data)
    assert Sms(header).CreatePremiumSubscription(
        body["CreatePremiumSubscription"]) == data, "should return an object"


@patch('requests.post')
def test_delete_premium_subscription(mock_post):
    data = responses['DeletePremiumSubscription']
    mock_post.return_value = R(data)
    assert Sms(header).DeletePremiumSubscription(
        body["DeletePremiumSubscription"]) == data, "should return an object"


@patch('requests.post')
def test_fetch_message(mock_post):
    data = responses['FetchMessage']
    mock_post.return_value = R(data)
    assert Sms(header).FetchMessage(
        body["FetchMessage"]) == data, "should return an object"


@patch('requests.post')
def test_fetch_premium_subscription(mock_post):
    data = responses['FetchPremiumSubscription']
    mock_post.return_value = R(data)
    assert Sms(header).FetchPremiumSubscription(
        body["FetchPremiumSubscription"]) == data, "should return an object"


@patch('requests.post')
def test_media_upload(mock_post):
    data = responses['MediaUpload']
    mock_post.return_value = R(data)
    assert Voice(header).MediaUpload(
        body["MediaUpload"]) == data, "should return an object"


@patch('requests.post')
def test_queue_status(mock_post):
    data = responses['QueueStatus']
    mock_post.return_value = R(data)
    assert Voice(header).QueueStatus(
        body["QueueStatus"]) == data, "should return an object"


@patch('requests.post')
def test_send_airtime(mock_post):
    data = responses['SendAirtime']
    mock_post.return_value = R(data)
    assert Airtime(header).SendAirtime(
        body["SendAirtime"]) == data, "should return an object"


@patch('requests.post')
def test_send_message(mock_post):
    data = responses['SendMessage']
    mock_post.return_value = R(data)
    assert Sms(header).SendMessage(
        body["SendMessage"]) == data, "should return an object"


@patch('requests.post')
def test_send_premium_message(mock_post):
    data = responses['SendPremiumMessage']
    mock_post.return_value = R(data)
    assert Sms(header).SendPremiumMessage(
        body["SendPremiumMessage"]) == data, "should return an object"


@patch('requests.post')
def test_voice_call(mock_post):
    data = responses['VoiceCall']
    mock_post.return_value = R(data)
    assert Voice(header).VoiceCall(
        body["VoiceCall"]) == data, "should return an object"
