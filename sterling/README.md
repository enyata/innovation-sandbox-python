# INNOVATION SANDBOX (Sterling)

## Common Credentials

Below is a list of required credentials.

### sandbox_key

This can be found in the innovation sandbox dashboard after sign up.

### host

This argument is optional in all cases. Defaults to `https://sandboxapi.fsi.ng` if not found.

### subscription_key

Subscription key which provides access to this API. Found in your Profile.

### Appid

Application ID

### ipval

ip value

## Header

The header is an argument passed when instantiating any object in this module

```python
 header = {
        "base_url": "your host ",
        "Sandbox-Key": "insert here your sandbox key",
		"Ocp-Apim-Subscription-Key": "t",
		"Ocp-Apim-Trace": "true",
		"Appid": "69",
		"Content-Type": "application/json",
		"ipval": "0"
    }
```

## Interbank Name Enquiry([options])

You can query and confirm account details using a valid NUBAN, in any bank.

### options

The module accepts options as an array of key-value.

#### params

Query Params

##### Referenceid

This is the unique number that identifies transactions/request.

##### RequestType

The is the type of the request being processed.

##### Translocation

GPS of the originating location of the transaction in longitude & latitude.

##### ToAccount

This is the NUBAN of the transaction recipient account.

##### destinationbankcode

This is the destination bank's code

### InnovationSandbox\Sterling\Transfer\InterbankNameEnquiry(credentials)

The credentials stated above will be passed as a query. The query parameter is passed as an argument to the named enquiry method. For example,

```python
from sterling.transfer import Transfer

query = {
        "Referenceid": "01",
        "RequestType": "01",
        "Translocation": "01",
        "ToAccount": "0037514056",
        "destinationbankcode": "00001"
    }

result = Transfer(header).InterbankNameEnquiry(query)

print(result)

```

## Interbank Transfer([options])

You can transfer funds from one bank or a financial institution to another.

### options

The module accepts options as array of key-value.

#### payload

Request Body

##### Referenceid

This is the unique number that identifies transactions/request.

##### RequestType

The is the type of request being processed.

##### SessionID

The is the session id.

##### FromAccount

This is the NUBAN of the transaction sender account.

##### ToAccount

This is the NUBAN of the transaction recipient account.

##### Amount

This is the amount sent.

##### Destinationbankcode

This is the destination bank's code

##### NEResponse

##### BenefiName

##### PaymentReference

##### OriginatorAccountName

##### translocation

### InnovationSandbox\Sterling\Account\InterbankTransferReq(credentials)

The credentials stated above will be passed as a body parameter. The body parameter is passed as an argument to the named enquiry method. For example,

```python
from sterling.account import Account
body = {
        "Referenceid": "0101",
        "RequestType": "0101",
        "Translocation": "0101",
        "SessionID": "01",
        "FromAccount": "01",
        "ToAccount": "01",
        "Amount": "01",
        "DestinationBankCode": "01",
        "NEResponse": "01",
        "BenefiName": "01",
        "PaymentReference": "01",
        "OriginatorAccountName": "01",
        "translocation": "01"
    }

result = Account(header).InterbankTransferReq(body)

print(result)

```
