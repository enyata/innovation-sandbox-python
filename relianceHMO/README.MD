# INNOVATION SANDBOX (RelianceHMO)

## Install

```bash
$ pip3 install innovation-sandbox
```

## Common Credentials

Below is a list of required credentials.

### Header

The header is an argument passed when instantiating any object in this module.

```python3
header = {
    "base_url": "https://sandboxapi.fsi.ng",
    "Sandbox-Key": "your-sandbox-key-here",
    "Content-Type": "application/json"
}
```

### body

The body is the payload data object that is sent along with the request.

## Clients Signup

You can sign up company and enrollees.

```python
from relianceHMO.clients import Clients

body = {
    "transfer_code": "1234WXYZ",
    "company_name": "Justice League",
    "company_address": "85, outer space",
    "state_code": "NG-LA",
    "payment_frequency": "monthly",
    "company_admin": {
        "first_name": "Bruce",
        "last_name": "Wayne",
        "email_address": "bruce@wayne.corp",
        "phone_number": "08011122234"
    },
    "enrollees": [
        {
            "plan_id": 22,
            "first_name": "Bruce",
            "last_name": "Wayne",
            "email_address": "bruce@wayne.corp",
            "phone_number": "08011122234"
        },
        {
            "plan_id": 14,
            "first_name": "Barry",
            "last_name": "Allen",
            "email_address": "barry@flash.org",
            "phone_number": "08033344322"
        }
    ]
}

header = {
    "base_url": "https://sandboxapi.fsi.ng",
    "Sandbox-Key": "your-sandbox-key-here",
    "Content-Type": "application/json"
}

result = Clients(header).SignupCompany(body)

print(result)
```

## Renew Client Subscription

You can renew signed up company and enrollees.

```python
from relianceHMO.clients import Clients

header = {
    "base_url": "https://sandboxapi.fsi.ng",
    "Sandbox-Key": "your-sandbox-key-here",
    "Content-Type": "application/json"
}

body = {
    "transfer_code": "1234WXYZ",
    "add": [
        {
            "plan_id": 22,
            "firstname": "Princess",
            "lastname": "Diana",
            "email": "diana@amazon.com",
            "phone_number": "08041122234"
        }
    ],
    "remove": [
        "K2JhMYr5wDGMxZWdh",
        "z44JhMYyDGMxZ362hwe"
    ],
    "update": [
        {
            "plan_id": 24,
            "user_token": "Y2JhMWJhNDc4YWJkMGMxZWdh"
        }
    ]
}

result = Clients(header).RenewSubscriptionCompany(body)

print(result)

```

## Consultations Request

Request consultation for enrollee.

```python
from relianceHMO.consultation import Consultation

header = {
    "base_url": "https://sandboxapi.fsi.ng",
    "Sandbox-Key": "your-sandbox-key-here",
    "Content-Type": "application/json"
}

params = {
    "patient_id": 232,
    "reason": 'reason for consultation'
}

result = Consultation(header).RequestConsultation(params)

print(result)

```

## Register Enrollees

Sign up individuals or buy multiple for families. Also supports bulk processing.

```python
from relianceHMO.enrollees import Enrollees

header = {
    "base_url": "https://sandboxapi.fsi.ng",
    "Sandbox-Key": "your-sandbox-key-here",
    "Content-Type": "application/json"
}

body = {
    "enrollees": [
        {
            "payment_frequency": "monthly",
            "first_name": "John",
            "last_name": "Doe",
            "email_address": "dewo.1@kang.pe",
            "phone_number": "08132846940",
            "plan_id": 22,
            "can_complete_profile": "true",
            "profile": {
                "sex": "m",
                "date_of_birth": "1991-03-03",
                "first_name": "Doey",
                "last_name": "Doe",
                "primary_phone_number": "08159049122",
                "home_address": "Somewhere Awesome",
                "has_smartphone": "true",
                "profile_picture_filename": "ttffddzp.jpg",
                "enrollee_type": 1,
                "hmo_id": ""
            },
            "dependants": [
                {
                    "first_name": "Janet",
                    "last_name": "Dependant",
                    "email_address": "wu1uo389@gmail.com",
                    "phone_number": "08132046940",
                    "plan_id": 22
                }
            ]
        }
    ]
}

result = Enrollees(header).Register(body)

print(result)

```

## Get Active Enrollees

To query all active enrollees.

```python
from relianceHMO.enrollees import Enrollees

header = {
    "base_url": "https://sandboxapi.fsi.ng",
    "Sandbox-Key": "your-sandbox-key-here",
    "Content-Type": "application/json"
}

params = {
    "page": 1,
    "limit": 10
}

result = Enrollees(header).GetAllEnrollee(params)

print(result)
```

## Get Single Enrollee

To query a single enrollee by id.

```python
from relianceHMO.enrollees import Enrollees

header = {
    "base_url": "https://sandboxapi.fsi.ng",
    "Sandbox-Key": "your-sandbox-key-here",
    "Content-Type": "application/json"
}

params = {
    "hmo_id": 'TXT/10002/A'
}

result = Enrollees(header).GetEnrollee(params)

print(result)

```

## Complete Enrollee Profile

Complete Enrollee’s profile.

```python
from relianceHMO.enrollees import Enrollees

header = {
    "base_url": "https://sandboxapi.fsi.ng",
    "Sandbox-Key": "your-sandbox-key-here",
    "Content-Type": "application/json"
}

params = {
    "sex": 'm',
    "date_of_birth": '1991-03-03',
    'home_address': "85, outer space",
    'has_smartphone': True,
    'profile_picture_filename': 'ttffddzp.png',
    'hash': 'ZDZhMTlYxRkQ0ODRDNisrMzQ'
}

result = Enrollees(header).Profile(body)

print(result)


```

## Enrollee Validation

Retrieve enrollee details.

```python
from relianceHMO.enrollees import Enrollees

header = {
    "base_url": "https://sandboxapi.fsi.ng",
    "Sandbox-Key": "your-sandbox-key-here",
    "Content-Type": "application/json"
}

params = {
    "hmo_id": 'TXT/10002/A'
}

result = Enrollees(header).Validate(params)

print(result)

```

## Enrollee ID Card

Retrieve enrollee id card image.

```python
from relianceHMO.enrollees import Enrollees

header = {
    "base_url": "https://sandboxapi.fsi.ng",
    "Sandbox-Key": "your-sandbox-key-here",
    "Content-Type": "application/json"
}

params = {
    "hmo_id": 'TXT/10002/A'
}

result = Enrollees(header).Card(params)

print(result)

```

## Get Plans

Get available plans.

```python
from relianceHMO.plans import Plans

header = {
    "base_url": "https://sandboxapi.fsi.ng",
    "Sandbox-Key": "your-sandbox-key-here",
    "Content-Type": "application/json"
}

params = {
    "type": 'individual',
    "package": 'corporate'
}

result = Plans(header).GetAllPlans(params)

print(result)

```

## Individual Signup

Sign up individuals or buy multiple for families. Also supports bulk processing.

```python
from relianceHMO.retails import Retails

header = {
    "base_url": "https://sandboxapi.fsi.ng",
    "Sandbox-Key": "your-sandbox-key-here",
    "Content-Type": "application/json"
}

body = {
    "Referral_code": "1122345",
    "enrollees": [
        {
            "payment_frequency": "monthly",
            "first_name": "John",
            "last_name": "Doe",
            "email_address": "testuser1@kang.pe",
            "phone_number": "08132646940",
            "plan_id": 22,
            "can_complete_profile": True,
            "dependants": [
                {
                    "first_name": "Janet",
                    "last_name": "Dependant",
                    "email_address": "testuser2@kang.pe",
                    "phone_number": "08132646940",
                    "plan_id": 22
                },
                {
                    "first_name": "Fred",
                    "last_name": "Dependant",
                    "email_address": "testuser3@kang.pe",
                    "phone_number": "08132646940",
                    "plan_id": 24
                }
            ]
        },
        {
            "payment_frequency": "q",
            "first_name": "Ben",
            "last_name": "Stiller",
            "email_address": "snr22325@awsoo.com",
            "phone_number": "08132646940",
            "plan_id": 24,
            "can_complete_profile": False,
            "dependants": []
        }
    ]
}
result = Retails(header).SignupIndividuals(body)

print(result)


```

## Renew Individual Subscription

Renew subscription for a single enrollee.

```python
from relianceHMO.retails import Retails

header = {
    "base_url": "https://sandboxapi.fsi.ng",
    "Sandbox-Key": "your-sandbox-key-here",
    "Content-Type": "application/json"
}

body = {
    "enrollees": [
        {
            "user_id": 345,
            "remove": [
                347
            ]
        }
    ]
}
result = Retails(header).Renew(body)

print(result)


```

## Get Healthcare Providers

Get Provider details. This can be used to provide more details of accessible hospitals for plans.

```python
from relianceHMO.utilities import Utilities

header = {
    "base_url": "https://sandboxapi.fsi.ng",
    "Sandbox-Key": "your-sandbox-key-here",
    "Content-Type": "application/json"
}

params = {
    "state": "NG-LA",
    "plan_id": 25,
    "tiers": 1,
    "page": 1,
    "limit": 50
}


result = Utilities(header).Providers(params)

print(result)

```

## Get States Available for Healthcare

Get states. This can be used to provide the state_id for client signup.

```python
from relianceHMO.utilities import Utilities

header = {
    "base_url": "https://sandboxapi.fsi.ng",
    "Sandbox-Key": "your-sandbox-key-here",
    "Content-Type": "application/json"
}

result = Utilities(header).States()

print(result)

```

## Benefit List

Retrieve Benefits list for Retail Plans.

```python
from relianceHMO.utilities import Utilities

header = {
    "base_url": "https://sandboxapi.fsi.ng",
    "Sandbox-Key": "your-sandbox-key-here",
    "Content-Type": "application/json"
}

params = {
    "plan": 25
}

result = Utilities(header).Benefits(params)

print(result)


```

## Get Titles

Get Titles for enrollee profile.

```python
from relianceHMO.utilities import Utilities

header = {
    "base_url": "https://sandboxapi.fsi.ng",
    "Sandbox-Key": "your-sandbox-key-here",
    "Content-Type": "application/json"
}

result = Utilities(header).Titles()

print(result)

```

## Get Occupations

Get Occupation(s) for enrollee profile.

```python
from relianceHMO.utilities import Utilities

header = {
    "base_url": "https://sandboxapi.fsi.ng",
    "Sandbox-Key": "your-sandbox-key-here",
    "Content-Type": "application/json"
}

result = Utilities(header).Occupations()

print(result)

```

## Get Marital Status(es)

Get Marital Status(es) for enrollee profile.

```python
from relianceHMO.utilities import Utilities

header = {
    "base_url": "https://sandboxapi.fsi.ng",
    "Sandbox-Key": "your-sandbox-key-here",
    "Content-Type": "application/json"
}

result = Utilities(header).GetMaritalStatus()

print(result)




```

## Wallet Balance

Get wallet balance - useful when you want to use the walleting system to pay (Company payment not supported with this method).

```python
from relianceHMO.wallet import Wallet

header = {
    "base_url": "https://sandboxapi.fsi.ng",
    "Sandbox-Key": "your-sandbox-key-here",
    "Content-Type": "application/json"
}

result = Wallet(header).WalletBalance()

print(result)

```

## Fund Wallet.

Fund Wallet.

```python
from relianceHMO.wallet import Wallet

header = {
    "base_url": "https://sandboxapi.fsi.ng",
    "Sandbox-Key": "your-sandbox-key-here",
    "Content-Type": "application/json"
}

body = {
    "amount": '250000'
}

result = Wallet(header).FundWallet(body)

print(result)
```

## Wallet Transactions.

Retrieve Wallet Transactions for client.

```python
from relianceHMO.wallet import Wallet

header = {
    "base_url": "https://sandboxapi.fsi.ng",
    "Sandbox-Key": "your-sandbox-key-here",
    "Content-Type": "application/json"
}


result = Wallet(header).PartnershipWalletTransactions()

print(result)
```
