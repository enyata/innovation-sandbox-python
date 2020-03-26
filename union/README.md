# INNOVATION SANDBOX (Union)

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

## Generate access token

A Token Generation message is a request to generate a one-time access code also known as token for a UBN-MiServe transaction.

```python
from union.token import Token

body =  {
"client_secret":  "secret",
"client_id":  "web01",
"grant_type":  "password",
"username":  "ubnclient01",
"password":  "w$777"

}

header =  {
"base_url":  "https://sandboxapi.fsi.ng",
"Content-Type":  "application/x-www-form-urlencoded",
"Sandbox-Key":  "your-sandbox-key-here"

}

result =  Token(header).AccessTokenGenerator(body)

print(result)
```

## Account Enquiry

This operation provides basic account information of CASA or GL.

```python3
from union.enquiry import Enquiry

body =  {
"accountNumber":  "0000791200",
"accountType":  "CASA"
}

params =  {
"access_token":  "your-access-token-here"
}

headers =  {
"base_url":  "https://sandboxapi.fsi.ng",
"Content-Type":  "application/json",
"Sandbox-Key":  "your-sandbox-key-here"
}

result =  Enquiry(headers).Account(body, params)

print(result)
```

## Customer Enquiry

This operation provides basic customer information of CASA or GL.

```python3
from union.enquiry import Enquiry

body =  {
"accountNumber":  "0000791200",
"accountType":  "CASA"
}

params =  {
"access_token":  "your-access-token-here"
}

headers =  {
"base_url":  "https://sandboxapi.fsi.ng",
"Content-Type":  "application/json",
"Sandbox-Key":  "your-sandbox-key-here"

}

result =  Enquiry(headers).Customer(body, params)

print(result)
```

## Customer and Account Enquiry

This operation enables client to do customer and account enquiry with a single call. The return message contains both customer and account information.

```python3
from union.enquiry import Enquiry

body =  {
"accountNumber":  "0000791200",
"accountType":  "CASA"

}

params =  {
"access_token":  "your-access-token-here"
}

headers =  {
"base_url":  "https://sandboxapi.fsi.ng",
"Content-Type":  "application/json",
"Sandbox-Key":  "your-sandbox-key-here"

}

result =  Enquiry(headers).CustomerAndAccount(body, params)

print(result)
```

## Change User Credentials

This operation enables client to change password.

```python
from union.user import User

body =  {
"username":  "user1",
"oldPassword":  "password2",
"password":  "password",
"moduleId":  "UNION_ONE",
"clientSecret":  "ABC"
}

params =  {
"access_token":  "your-access-token-here"
}

header =  {
"base_url":  "https://sandboxapi.fsi.ng",
"Content-Type":  "application/json",
"Sandbox-Key":  "your-sandbox-key-here"
}

result =  User(header).ChangeUsersCredentials(body, params)

print(result)
```
