import unittest
from unittest.mock import Mock, patch
from .common import header, params, body, responses, R
from relianceHMO.enrollees import Enrollees
from relianceHMO.clients import Clients
from relianceHMO.retails import Retails
from relianceHMO.utilities import Utilities
from relianceHMO.wallet import Wallet
from relianceHMO.plans import Plans
from relianceHMO.consultation import Consultation


@patch('requests.post')
def test_signup_company(mock_post):
    data = responses['SignupCompany']
    mock_post.return_value = R(data)
    assert Clients(header).SignupCompany(
        body["SignupCompany"]) == data, "should return an object"


@patch('requests.put')
def test_renew_subscription_company(mock_post):
    data = responses['RenewSubscriptionCompany']
    mock_post.return_value = R(data)
    assert Clients(header).RenewSubscriptionCompany(
        body["RenewSubscriptionCompany"]) == data, "should return an object"


@patch('requests.post')
def test_request_consultation(mock_post):
    data = responses['RequestConsultation']
    mock_post.return_value = R(data)
    assert Consultation(header).RequestConsultation(
        params["RequestConsultation"]) == data, "should return an object"


@patch('requests.post')
def test_register_enrollees(mock_post):
    data = responses['RegisterEnrollees']
    mock_post.return_value = R(data)
    assert Enrollees(header).Register(
        body["RegisterEnrollees"]) == data, "should return an object"


# @patch('requests.post')
# def test_get_all_enrollee(mock_post):
#     data = responses['GetAllEnrollee']
#     mock_post.return_value = R(data)
#     assert Enrollees(header).GetAllEnrollee(
#         params["GetAllEnrollee"]) == data, "should return an object"


# @patch('requests.post')
# def test_get_enrollee(mock_post):
#     data = responses['GetEnrollee']
#     mock_post.return_value = R(data)
#     assert Enrollees(header).GetEnrollee(
#         params["GetEnrollee"]) == data, "should return an object"


# @patch('requests.post')
# def test_complete_enrollee_profile(mock_post):
#     data = responses['CompleteEnrolleeProfile']
#     mock_post.return_value = R(data)
#     assert Enrollees(header).Profile(
#         params["CompleteEnrolleeProfile"]) == data, "should return an object"


# @patch('requests.post')
# def test_enrollee_validation(mock_post):
#     data = responses['EnrolleesValidation']
#     mock_post.return_value = R(data)
#     assert Enrollees(header).Validate(
#         params["EnrolleesValidation"]) == data, "should return an object"


# @patch('requests.post')
# def test_enrollee_id_card(mock_post):
#     data = responses['EnrolleesIDCard']
#     mock_post.return_value = R(data)
#     assert Enrollees(header).Card(
#         params["EnrolleesIDCard"]) == data, "should return an object"


@patch('requests.get')
def test_get_all_plans(mock_post):
    data = responses['GetAllPlans']
    mock_post.return_value = R(data)
    assert Plans(header).GetAllPlans(
        params["GetAllPlans"]) == data, "should return an object"


@patch('requests.post')
def test_individual_signup(mock_post):
    data = responses['IndividualSignup']
    mock_post.return_value = R(data)
    assert Retails(header).SignupIndividuals(
        body["IndividualSignup"]) == data, "should return an object"


# @patch('requests.post')
# def test_renew_subscription_signup(mock_post):
#     data = responses['RenewSubscriptionIndividuals']
#     mock_post.return_value = R(data)
#     assert Retails(header).Renew(
#         body["RenewSubscriptionIndividuals"]) == data, "should return an object"


@patch('requests.get')
def test_get_health_care_providers(mock_post):
    data = responses['GetHealthcareProviders']
    mock_post.return_value = R(data)
    assert Utilities(header).Providers(
        params["GetHealthcareProviders"]) == data, "should return an object"


@patch('requests.get')
def test_get_states_available(mock_post):
    data = responses['GetStatesAvailable']
    mock_post.return_value = R(data)
    assert Utilities(header).States() == data, "should return an object"


@patch('requests.get')
def test_benefit_list(mock_post):
    data = responses['BenefitsList']
    mock_post.return_value = R(data)
    assert Utilities(header).Benefits(
        params["BenefitsList"]) == data, "should return an object"


@patch('requests.get')
def test_get_titles(mock_post):
    data = responses['GetTitles']
    mock_post.return_value = R(data)
    assert Utilities(header).Titles() == data, "should return an object"


@patch('requests.get')
def test_get_occupations(mock_post):
    data = responses['GetOccupations']
    mock_post.return_value = R(data)
    assert Utilities(header).Occupations() == data, "should return an object"


@patch('requests.get')
def test_get_marital_status(mock_post):
    data = responses['GetMaritalStatus']
    mock_post.return_value = R(data)
    assert Utilities(header).GetMaritalStatus(
    ) == data, "should return an object"


# @patch('requests.post')
# def test_wallet_balance(mock_post):
#     data = responses['WalletBalance']
#     mock_post.return_value = R(data)
#     assert Wallet(header).WalletBalance() == data, "should return an object"


@patch('requests.post')
def test_fund_wallet(mock_post):
    data = responses['FundWallet']
    mock_post.return_value = R(data)
    assert Wallet(header).FundWallet(
        body["FundWallet"]) == data, "should return an object"


@patch('requests.get')
def test_partnership_wallet_transactions(mock_post):
    data = responses['PartnershipWalletTransactions']
    mock_post.return_value = R(data)
    assert Wallet(header).PartnershipWalletTransactions(
    ) == data, "should return an object"
