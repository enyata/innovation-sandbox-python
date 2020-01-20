
Innovation Sandbox (Python)
===========================

| A Python module that gives access to the innovation sandbox API on the go!

Features
~~~~~~~~

* Super easy to use
* Very easy to understand
* Get the code right in your editor

Installation
~~~~~~~~~~~~

* Just fire the following command in your terminal:

::

   pip3 install innovation-sandbox

- | It's that easy. If you are using Python 2.7 use pip instead. Depending on your
  | permissions, you might need to use ``pip install --user innovation-sandbox`` to install.

* Or you can download the source code from `here <https://github.com/enyata/innovation-sandbox-python>`_, and then just install the package using

::

    python setup.py install

~~~~~~~~~~~~~~~~~

* to use the Request module, which takes the header parameters as a dictionary

.. code:: python

    >>>from nibss.request import Request

    header = {
        "base_url": "",
        "Organizationcode": YOUR_ORGANIZATION_CODE,
        "sandbox-key": YOUR_SANDBOX_KEY,
        "content-type": "application/json",
        "accept": "application/json",
        "username": YOUR_ORGANIZATION_CODE,
        "password": YOUR_PASSWORD
      }

    request = Request(header)

# The base URL for all API endpoints in the sandbox can be passed as a header parameter, else it results to a default as given below:
    ``https://innovation-sandbox-backend.herokuapp.com``

# For Organization Code, use ``11111`` for testing purposes

*  to reset sandbox credentials

.. code:: python

    >>> from nibss.request import Request

    reset = request.sandbox_reset()
    >>>print(reset)
    {'aes_key': '9+CZaWqfyI/fwezX', 'password': "^o'e6EXK5T ~^j2=", 'ivkey': 'eRpKTBjdOq6T67D0'}


* To Verify a single BVN

.. code:: python

    >>> from nibss.request import Request

    verify_single = request.verify_single({
                                "body":{"BVN": "12345678901"},
                                "Aes_key":"9+CZaWqfyI/fwezX",
                                "Iv_key":"eRpKTBjdOq6T67D0"
                            })
    >>>print(verify_single)
    {
            'message': 'OK',
            'data': {'ResponseCode': '00', 'BVN': '12345678901', 'FirstName': 'Uchenna', 'MiddleName': 'Chijioke',
                     'LastName': 'Nwanyanwu', 'DateOfBirth': '22-Oct-1970', 'PhoneNumber': '07033333333',
                     'RegistrationDate': '16-Nov-2014', 'EnrollmentBank': '900',
                     'EnrollmentBranch': 'Victoria Island', 'WatchListed': 'NO'}
    }

* To Verify a multiple BVN

.. code:: python

    >>> from nibss.request import Request

    verify_multiple = request.verify_multiple({
                                "bvns":{"BVNS": "1234567890 1, 12345678902, 12345678903"},
                                "Aes_key":"9+CZaWqfyI/fwezX",
                                "Iv_key":"eRpKTBjdOq6T67D0"
                            })
    >>>print(verify_multiple)
    {
            "message": "OK", "data": {"ResponseCode": "00", "ValidationResponses": [
                {"ResponseCode": "00", "BVN": "12345678901", "FirstName": "Uchenna", "MiddleName": "Innocent",
                 "LastName": "Nwanyanwu", "DateOfBirth": "29-Oct-1995", "PhoneNumber": "07033333333",
                 "RegistrationDate": "16-Dec-2014", "EnrollmentBank": "900", "EnrollmentBranch": "Victoria Island",
                 "WatchListed": "NO"},
                {"ResponseCode": "00", "BVN": "12345678902", "FirstName": "Wale", "MiddleName": "Joshua",
                 "LastName": "Odugbemi", "DateOfBirth": "29-Oct-1996", "PhoneNumber": "07033333334",
                 "RegistrationDate": "16-Oct-2014", "EnrollmentBank": "900",
                 "EnrollmentBranch": "No. 2 NIBSS Avenue, VI",
                 "WatchListed": "YES"},
                {"ResponseCode": "00", "BVN": "12345678903", "FirstName": "Seun", "MiddleName": "Ogunjimi",
                 "LastName": "Isaiah", "DateOfBirth": "29-Oct-1997", "PhoneNumber": "07033333336",
                 "RegistrationDate": "16-Sept-2014", "EnrollmentBank": "900", "EnrollmentBranch": "Ikorodu",
                 "WatchListed": "NO"}]}
    }

* To Verify a check if a BVN is watchlisted

.. code:: python

    >>> from nibss.request import Request

    watchlisted = request.bvn_watchlisted({
                                "body":{"BVN": "12345678901"},
                                "Aes_key":"9+CZaWqfyI/fwezX",
                                "Iv_key":"eRpKTBjdOq6T67D0"
                            })
    >>>print(watchlisted)
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

    >>> from nibss.request import Request

    placeholder_reset = request.bvn_placeholder_reset()
    >>>print(placeholder_reset)
    {'aes_key': '9+CZaWqfyI/fwezX', 'password': "^o'e6EXK5T ~^j2=", 'ivkey': 'eRpKTBjdOq6T67D0'}

* To Validate a Record

.. code:: python

    >>> from nibss.request import Request

    validated_record = request.validate_record({"body":{
                                    "BVN": "12345678901",
                                    "FirstName": "Uchenna",
                                    "LastName": "Okoro",
                                    "MiddleName": "Adepoju",
                                    "AccountNumber": "0987654321",
                                    "BankCode": "011"
                                }, "Aes_key":"9+CZaWqfyI/fwezX", "Iv_key":"eRpKTBjdOq6T67D0"})
    >>>print(validated_record)
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

    >>> from nibss.request import Request

    validated_records = request.validate_records({"body":[
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
        ], "Aes_key":"9+CZaWqfyI/fwezX", "Iv_key":"eRpKTBjdOq6T67D0"})
    >>>print(validated_records)
    {
            'message': 'OK',
            'data': {'ValidationResponses': [
                {
                    'ResponseCode': '00',
                    'BVN': 'VALID',
                    'FirstName': 'VALID',
                    'LastName': 'VALID',
                    'MiddleName': 'INVALID',
                    'AccountNumber': 'VALID',
                    'BankCode': 'VALID'},
                {
                    'ResponseCode': '00', 'BVN': 'VALID', 'FirstName': 'INVALID', 'LastName': 'VALID',
                    'MiddleName': 'INVALID', 'AccountNumber': 'VALID', 'BankCode': 'VALID'
                }]}}

* To Verify finger print

.. code:: python

    >>> from nibss.request import Request

    fingerprint_records = request.verify_fingerprint({"body":{
            "BVN": "12345678901",
            "DeviceId": "Z000112BC12",
            "ReferenceNumber": "00099201710012205354422",
            "FingerImage": {
                "type": "ISO_2005",
                "position": "RT",
                "nist_impression_type": "0",
                "value": "c2RzZnNkZnNzZGY="
            }
        }, "Aes_key":"9+CZaWqfyI/fwezX", "Iv_key":"eRpKTBjdOq6T67D0"})
    >>>print(fingerprint_records)
    {
            "message": "OK",
            "data": {
                "BVN": "12345678901",
                "ResponseCode": "00"
            }
        }