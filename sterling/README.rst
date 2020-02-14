Innovation Sandbox (Sterling)
==============================

| A Python module that gives access to the Sterling API on the go!

Header
~~~~~~~~
* The header is an argument passed when instantiating any object in this module

.. code:: python

    header = {
        "base_url": "",
        "Sandbox-Key": "insert here your sandbox key",
		"Ocp-Apim-Subscription-Key": "Subscription key which provides access to this API. Found in your Profile",
		"Ocp-Apim-Trace": "Ocp-Apim-Trace",
		"Appid": "Application ID",
		"Content-Type": "application/json",
		"ipval": "ip value"
    }

# The base URL for all API endpoints in the sandbox can be passed as a header parameter, else it results to a default as given below:
    ``https://sandboxapi.fsi.ng``

Query Parameters
~~~~~~~~~~~~~~~~~
* The query parameter is passed as an argument to the name enquiry method.

.. code:: python

    query = {
        "Referenceid": "This is the unique number that identifies transactions/request.",
        "RequestType": "The is the identity of the request being processed",
        "Translocation": "GPS of the originating location of the transaction in longitude & latitude",
        "ToAccount": "This is the nuban of the transaction recipient account.",
        "destinationbankcode": "This is the destination bank's code"
    }

~~~~~~~~~~~~~~~~~

*  For interbank name enquiry

.. code:: python

    >>> from sterling.transfer import Transfer

    result = Transfer(header).InterbankNameEnquiry(query)

    >>> print(result)
    {
    "message": "OK",
    "data": {
        "message": "success",
        "response": "success",
        "data": {
            "AccountName": "John Doe",
            "sessionID": "999232200107170915323048583333",
            "AccountNumber": " 0037514056",
            "status": "97",
            "BVN": "12345678901",
            "ResponseText" : null
            }
        }
    }

*  For interbank Transfer

.. code:: python

    >>> from sterling.account import Account

    body = {
        "Referenceid": "PROVIDE REFERENCE ID",
        "RequestType": "PROVIDE REQUEST TYPE",
        "Translocation": "PROVIDE TRANSLOCATION",
        "SessionID": "PROVIDE SESSION ID",
        "FromAccount": "FROM ACCOUNT",
        "ToAccount": "PROVIDE DESTINATION ACCOUNT",
        "Amount": "AMOUNT",
        "DestinationBankCode": "DESTINATION CODE",
        "NEResponse": "RESPONSE",
        "BenefiName": "BENEFACTORS NAME",
        "PaymentReference": "PAYMENT REFERENCE",
        "OriginatorAccountName": "ORIGINATOR ACCOUNT NAME",
        "translocation": "TRANSLOCATION"
    }
    result = Account(header).InterbankTransferReq(body)

    >>> print(result)
    {
    "message": "OK",
    "data": {
        "message": "success",
        "response": "success",
        "data": {
            "AccountName": "John Doe",
            "sessionID": "999232200107170915323048583333",
            "AccountNumber": " 0037514056",
            "status": "97",
            "BVN": "12345678901",
            "ResponseText" : null
            }
        }
    }

Tests
~~~~~

* Just type in the following command to run the tests

.. code:: bash

    py.test

* This will run the test defined in the files of the ``tests/`` directory
