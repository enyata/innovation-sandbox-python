INNOVATION SANDBOX (NIBSS)
==========================

Install
-------

.. code:: bash


    $ pip3 install innovation-sandbox

RESET\_TOKEN([Options])
-----------------------

This should be done on every initialization.

Options
~~~~~~~

The module accepts options as an array of key-value and returns
aes\_key, ivkey and password.

sandbox\_key
^^^^^^^^^^^^

This can be found in the innovation sandbox dashboard after sign up.

organisation\_code
^^^^^^^^^^^^^^^^^^

This credential is gotten from NIBSS prior to acquiring this credential,
11111 should be used for testing.

base\_url
^^^^^^^^^

This argument is optional in all cases. Defaults to
``https://sandboxapi.fsi.ng`` if not found.

Header
^^^^^^

This is to be sent along for every request made, it contains the
credentials mentioned above. An example,

.. code:: python3

    header = {
        "base_url": "your host",
        "Organizationcode": "11111",
        "sandbox-key": "your sandbox_key",
        "content-type": "application/json",
        "accept": "application/json",
        "username": "your organization code or 11111",
        "password": ""
    }

reset(credentials)
~~~~~~~~~~~~~~~~~~

Returns the aes\_key, ivey and password. As earlier stated this function
should be called at every initialization. The credentials returned is
set as part of the data for accessing other NIBSS modules.

The following example calls the reset module

.. code:: python3

    from nibss.credentials import Credentials

    reset = Credentials(header).reset()

    print(reset)

Below is an example of a reset result:

.. code:: python3

    {
      'password': 'password',
      'ivkey': 'Your ivykey',
      'aes_key': 'Your aes_key'
    }

USING CREDENTIALS
-----------------

Once the credentials from the reset module has been acquired it should
be appended as an array alongside the organization\_code, host and
sandbox\_key as part of the credentials to every request made to the
NIBSS API.

Verify Single BVN
~~~~~~~~~~~~~~~~~

Verifies single BVN

verify\_single(credentials)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

In additions to the credentials stated above a 'bvn' key with the value
of the bvn number to be verified as a string should be added to the
request. For example

.. code:: python3

    from nibss.bvn import Bvn

    verify_single = Bvn(header).verify_single({
        "body":{"BVN": "12345678901"},
        "Aes_key": "YOUR_AES_KEY",
        "Iv_key": "YOUR_IV_KEY"
    })

    print(verify_single)

Verify Multiple BVN
~~~~~~~~~~~~~~~~~~~

Verifies more than one BVN

verify\_multiple(credentials)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Credentials are same as verify\_single. The BVNs are separated by comma.
For example

.. code:: python3

    from nibss.bvn import Bvn

    verify_multiple = Bvn(header).verify_multiple({
        "bvns":{"BVNS": "12345678901, 12345678902, 12345678903"},
        "Aes_key": "YOUR_AES_KEY",
        "Iv_key": "YOUR_IV_KEY"
    })

    print(verify_multiple)

Note: This module accepts a maximum of 10 BVNs as the bvn value.

GET SINGLE BVN
~~~~~~~~~~~~~~

Gets single BVN

get\_single(credentials)
^^^^^^^^^^^^^^^^^^^^^^^^

Credentials are same as verify\_single.

.. code:: python3

    from nibss.bvn import Bvn

    get_single = Bvn(header).get_single({
        "body":{"BVN": "12345678901"},
        "Aes_key": "YOUR_AES_KEY",
        "Iv_key": "YOUR_IV_KEY"
    })

    print(get_single)

GET Multiple BVN
~~~~~~~~~~~~~~~~

Gets multiple BVN

get\_multiple(credentials)
^^^^^^^^^^^^^^^^^^^^^^^^^^

Credentials are same as verify\_multiple.

.. code:: python3

    from nibss.bvn import Bvn

    get_multiple = Bvn(header).get_multiple({
        "bvns":{"BVNS": "12345678901, 12345678902, 12345678903"},
        "Aes_key": "YOUR_AES_KEY",
        "Iv_key": "YOUR_IV_KEY"
    })

    print(get_multiple)

Is BVN Watchlisted
~~~~~~~~~~~~~~~~~~

Verifies if BVN has been watch listed.

watchlisted(credentials)
^^^^^^^^^^^^^^^^^^^^^^^^

Credentials are same as verify\_single.

.. code:: python3

    from nibss.bvn import Bvn

    watchlisted = Bvn(header).bvn_watchlisted({
        "body":{"BVN": "12345678901"},
        "Aes_key": "YOUR_AES_KEY",
        "Iv_key": "YOUR_IV_KEY"
    })

    print(watchlisted)

Verify Finger Print
~~~~~~~~~~~~~~~~~~~

Verifies finger print

fingerprint\_record(credentials)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Credentials are same as verify\_single. Below is an example on how to
verify finger print

.. code:: python3

    from nibss.fingerprint import FingerPrint

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
            "Aes_key": "YOUR_AES_KEY",
            "Iv_key": "YOUR_IV_KEY"
        }
    )

    print(fingerprint_records)

Validate Single Record
~~~~~~~~~~~~~~~~~~~~~~

Validates single record

validated\_record(credentials)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Credentials are same as verify\_single.

.. code:: python3

    from nibss.records import Record

    validated_record = Record(header).validate_record({
        "body":{
        "BVN": "12345678901",
        "FirstName": "Uchenna",
        "LastName": "Okoro",
        "MiddleName": "Adepoju",
        "AccountNumber": "0987654321",
        "BankCode": "011"
        },
        "Aes_key": "YOUR_AES_KEY",
        "Iv_key": "YOUR_IV_KEY"
    })

    print(validated_record)

Validate Multiple Records
~~~~~~~~~~~~~~~~~~~~~~~~~

Validates multiple records

validated\_records(credentials)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Credentials are same as verify\_single.

.. code:: python3

    from nibss.records import Record

    validated_records = Record(header).validate_records({
        "body":
        [
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
            "Aes_key": "YOUR_AES_KEY",
            "Iv_key": "YOUR_IV_KEY"
        }
    )

    print (validated_records)

