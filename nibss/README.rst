
Innovation Sandbox (Nibss)
===========================

| A Python module that gives access to the NIBSS API on the go!

Header
~~~~~~~~
* The header is an argument passed when instantiating any object in this module

.. code:: python

    header = {
        "base_url": "",
        "Organizationcode": YOUR_ORGANIZATION_CODE,
        "sandbox-key": YOUR_SANDBOX_KEY,
        "content-type": "application/json",
        "accept": "application/json",
        "username": YOUR_ORGANIZATION_CODE,
        "password": YOUR_PASSWORD
    }

# The base URL for all API endpoints in the sandbox can be passed as a header parameter, else it results to a default as given below:
    ``https://sandboxapi.fsi.ng``

~~~~~~~~~~~~~~~~~

*  to reset sandbox credentials

.. code:: python

    >>> from nibss.credentials import Credentials

    reset = Credentials(header).reset()

    >>> print(reset)
    {'aes_key': 'mbhfydxfxcx', 'password': "mjhgyugftd", 'ivkey': 'nbvgxdrxzre'}


* To Verify a single BVN

.. code:: python

    >>> ffrom nibss.bvn import Bvn

    verify_single = Bvn(header).verify_single({
        "body":{"BVN": "12345678901"},
        "Aes_key": YOUR_AES_KEY,
        "Iv_key": YOUR_IV_KEY
    })

    >>> print(verify_single)
    {
        'message': 'OK',
        'data': {
            'ResponseCode': '00',
            'BVN': '12345678901',
            'FirstName': 'Uchenna',
            'MiddleName': 'Chijioke',
            'LastName': 'Nwanyanwu',
            'DateOfBirth': '22-Oct-1970',
            'PhoneNumber': '07033333333',
            'RegistrationDate': '16-Nov-2014',
            'EnrollmentBank': '900',
            'EnrollmentBranch': 'Victoria Island',
            'WatchListed': 'NO'
        }
    }

# YOUR_AES_KEY and YOUR_IV_KEY are same as the ones given after calling ``reset()`` to reset sandbox credentials

* To Verify a multiple BVN

.. code:: python

    >>> from nibss.bvn import Bvn

    verify_multiple = Bvn(header).verify_multiple({
        "bvns":{"BVNS": "12345678901, 12345678902, 12345678903"},
        "Aes_key": YOUR_AES_KEY,
        "Iv_key": YOUR_IV_KEY
    })

    >>> print(verify_multiple)
    {
        "message": "OK",
        "data": {
            "ResponseCode": "00",
            "ValidationResponses": [
            {
                "ResponseCode": "00",
                "BVN": "12345678901",
                "FirstName": "Uchenna",
                "MiddleName": "Innocent",
                "LastName": "Nwanyanwu",
                "DateOfBirth": "29-Oct-1995",
                "PhoneNumber": "07033333333",
                "RegistrationDate": "16-Dec-2014",
                "EnrollmentBank": "900",
                "EnrollmentBranch": "Victoria Island",
                "WatchListed": "NO"
            },
            {
                "ResponseCode": "00",
                "BVN": "12345678902",
                "FirstName": "Wale",
                "MiddleName": "Joshua",
                "LastName": "Odugbemi",
                "DateOfBirth": "29-Oct-1996",
                "PhoneNumber": "07033333334",
                "RegistrationDate": "16-Oct-2014",
                "EnrollmentBank": "900",
                "EnrollmentBranch": "No. 2 NIBSS Avenue, VI",
                "WatchListed": "YES"
            },
            {
                "ResponseCode": "00",
                "BVN": "12345678903",
                "FirstName": "Seun",
                "MiddleName": "Ogunjimi",
                "LastName": "Isaiah",
                "DateOfBirth": "29-Oct-1997",
                "PhoneNumber": "07033333336",
                "RegistrationDate": "16-Sept-2014",
                "EnrollmentBank": "900",
                "EnrollmentBranch": "Ikorodu",
                "WatchListed": "NO"
            }]
        }
    }

* To Verify a check if a BVN is watchlisted

.. code:: python

    >>> from nibss.bvn import Bvn

    watchlisted = Bvn(header).bvn_watchlisted({
        "body":{"BVN": "12345678901"},
        "Aes_key": YOUR_AES_KEY,
        "Iv_key": YOUR_IV_KEY
    })

    >>> print(watchlisted)
    {
        "message": "OK",
        "data": {
            "ResponseCode": "00",
            "BVN": "12345678901",
            "BankCode": "900",
            "Category": "1",
            "WatchListed": "YES"
        }
    }

* To Reset Placeholder

.. code:: python

    >>> from nibss.placeholder import PlaceHolder

    placeholder_reset = PlaceHolder(header).bvn_placeholder_reset()

    >>> print(placeholder_reset)
    {'aes_key': '9+CZaWqfyI/fwezX', 'password': "^o'e6EXK5T ~^j2=", 'ivkey': 'eRpKTBjdOq6T67D0'}

* To Validate a Record

.. code:: python

    >>> from nibss.records import Record

    validated_record = Record(header).validate_record({
        "body":{
        "BVN": "12345678901",
        "FirstName": "Uchenna",
        "LastName": "Okoro",
        "MiddleName": "Adepoju",
        "AccountNumber": "0987654321",
        "BankCode": "011"
        }, "Aes_key": YOUR_AES_KEY,
        "Iv_key": YOUR_IV_KEY
    })

    >>> print(validated_record)
    {
        "message": "OK",
        "data": {
            "ResponseCode": "00",
            "BVN": "VALID",
            "FirstName": "VALID",
            "LastName": "VALID",
            "MiddleName": "INVALID",
            "AccountNumber": "VALID",
            "BankCode": "VALID"
        }
    }

* To Validate Records

.. code:: python

    >>> from nibss.records import Record

    validated_records = Record(header).validate_records({
        "body":[
        {
            "BVN": "12345678901",
            "FirstName": "Uchenna",
            "LastName": "Okoro",
            "MiddleName": "Adepoju",
            "AccountNumber": "0987654321",
            "BankCode": "011"
        },
        {
            "BVN": "12345678912",
            "FirstName": "Chidi",
            "LastName": "Seun",
            "MiddleName": "Joshua",
            "AccountNumber": "0987654329",
            "BankCode": "012"
        }
        ],
        "Aes_key": YOUR_AES_KEY,
        "Iv_key": YOUR_IV_KEY
    })

    >>> print (validated_records)
    {
        'message': 'OK',
        'data': {
            'ValidationResponses': [
            {
                'ResponseCode': '00',
                'BVN': 'VALID',
                'FirstName': 'VALID',
                'LastName': 'VALID',
                'MiddleName': 'INVALID',
                'AccountNumber': 'VALID',
                'BankCode': 'VALID'},
            {
                'ResponseCode': '00',
                'BVN': 'VALID',
                'FirstName': 'INVALID',
                'LastName': 'VALID',
                'MiddleName': 'INVALID',
                'AccountNumber': 'VALID',
                'BankCode': 'VALID'
            }]
        }
    }

* To Verify finger print

.. code:: python

    >>> from nibss.fingerprint import FingerPrint

    fingerprint_records = FingerPrint(header).verify_fingerprint(
    {
        "body":{
            "BVN": "12345678901",
            "DeviceId": "Z000112BC12",
            "ReferenceNumber": "00099201710012205354422",
            "FingerImage": {
                "type": "ISO_2005",
                "position": "RT",
                "nist_impression_type": "0",
                "value": "c2RzZnNkZnNzZGY="
            }
        },
        "Aes_key": YOUR_AES_KEY,
        "Iv_key": YOUR_IV_KEY
    })
    >>> print(fingerprint_records)
    {
        "message": "OK",
        "data": {
            "BVN": "12345678901",
            "ResponseCode": "00"
        }
    }

Tests
~~~~~

* Just type in the following command to run the tests

.. code:: bash

    py.test

* This will run the test defined in the files of the ``tests/`` directory

