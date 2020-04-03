INNOVATION SANDBOX (Atlabs)
===========================

Install
-------

.. code:: bash

    $ pip3 install innovation-sandbox

Common Credentials
------------------

Below is a list of required credentials.

Header
~~~~~~

The header is an argument passed when instantiating any object in this
module.

.. code:: python3

    header = {
        "base_url": "https://sandboxapi.fsi.ng",
        "Sandbox-Key": "your-sandbox-key-here",
        "Content-Type": "application/json"
    }

body
~~~~

The body is the payload data object that is sent along with the request.

Create Checkout Token
---------------------

To create a new checkout token.

phoneNumber
^^^^^^^^^^^

The phone number to be subscribed.

.. code:: python3

    from atlabs.token import Token

    header = {
        "base_url": "https://sandboxapi.fsi.ng",
        "Sandbox-Key": "your-sandbox-key-here",
        "Content-Type": "application/json"
    }

    body = {
        "phoneNumber": "+2348123456789"
    }

    result = Token(header).CreateCheckoutToken(body)

    print(result)

Voice Call
----------

Initiate a phone call

callFrom
^^^^^^^^

Your Africa's Talking issued virtual phone number.

callTo
^^^^^^

Phone number to dial

.. code:: python3

    from atlabs.voice import Voice

    header = {
        "base_url": "https://sandboxapi.fsi.ng",
        "Sandbox-Key": "your-sandbox-key-here",
        "Content-Type": "application/json"
    }

    body = {
        "callFrom": "FSI",
        "callTo": "+2348123456789"
    }

    result = Voice(header).VoiceCall(body)
    print(result)

Fetch Queue Calls
-----------------

Get queued calls

phoneNumbers
^^^^^^^^^^^^            

Your Africa's Talking issued virtual phone number.

.. code:: python3

    from atlabs.voice import Voice

    header = {
        "base_url": "https://sandboxapi.fsi.ng",
        "Sandbox-Key": "your-sandbox-key-here",
        "Content-Type": "application/json"
    }

    body = {
        "phoneNumbers": "+2348123456789"
    }

    result = Voice(header).QueueStatus(body)
    print(result)

Upload Media File
-----------------

You can upload media/audio file with the extension .mp3 or .wav only.
This media files will be played when called upon by one of our voice
actions.

phoneNumbers
^^^^^^^^^^^^

Your Africa's Talking issued virtual phone number.

url
^^^

URL to your media file

.. code:: python3

    from atlabs.voice import Voice

    header = {
        "base_url": "https://sandboxapi.fsi.ng",
        "Sandbox-Key": "your-sandbox-key-here",
        "Content-Type": "application/json"
    }

    body = {
        "phoneNumber": "+2348123456789",
        "url": "http://url-to-media-file.mp3"
    }

    result = Voice(header).MediaUpload(body)
    print(result)

SMS Service
-----------

You can send SMS by making a HTTP POST request to the SMS API.

to
^^

A String or an array with comma separated string of recipients’ phone
numbers.

from
^^^^

Your registered short code or alphanumeric, defaults is FSI.

message
^^^^^^^

The message to be sent.

enqueue (optional)
^^^^^^^^^^^^^^^^^^

Set to true if you would like to deliver as many messages to the API
without waiting for an acknowledgement from telecom companies.

.. code:: python3

    from atlabs.sms import Sms

    header = {
        "base_url": "https://sandboxapi.fsi.ng",
        "Sandbox-Key": "your-sandbox-key-here",
        "Content-Type": "application/json"
    }

    body = {
        "to": "+2348123456789",
        "from": "FSI",
        "message": "Hello world!"
    }

    result = Sms(header).SendSms(body)
    print(result)

Premium Subscription
--------------------

To send premium SMS.

to
^^

A String or an array with comma separated string of recipients’ phone
numbers.

from
^^^^

Your registered short code or alphanumeric, defaults is FSI.

message
^^^^^^^

The message to be sent.

keyword
^^^^^^^

Your premium product keyword "innovation-sandbox".

linkId
^^^^^^

We forward the linkId to your application when the user send a message
to your service.

retryDurationInHours
^^^^^^^^^^^^^^^^^^^^

It specifies the number of hours your subscription message should be
retried in case it's not delivered to the subscriber.

.. code:: python3

    from atlabs.sms import Sms

    header = {
        "base_url": "https://sandboxapi.fsi.ng",
        "Sandbox-Key": "your-sandbox-key-here",
        "Content-Type": "application/json"
    }

    body = {
        "to": "+2348123456789",
        "from": "FSI",
        "message": "Hello world!",
        "keyword": "innovation-sandbox",
        "linkId": "d",
        "retryDurationInHours": 1
    }

    result = Sms(header).SendPremiumSms(body)
    print(result)

Create Premium Subscription
---------------------------

To create a premium subscription, you first need to create a
checkoutToken.

shortCode
^^^^^^^^^

This is the premium short code mapped to your account.

keyword
^^^^^^^

Your premium product keyword.

phoneNumber
^^^^^^^^^^^ 

The phone number to be subscribed.

checkoutToken
^^^^^^^^^^^^^

This is a token used to validate the subscription request and can only
be used once. Generate one from checkoutToken.

.. code:: python3

    from atlabs.sms import Sms

    header = {
        "base_url": "https://sandboxapi.fsi.ng",
        "Sandbox-Key": "your-sandbox-key-here",
        "Content-Type": "application/json"
    }

    body = {
        "shortCode": "19171",
        "keyword": "innovation-sandbox",
        "phoneNumber": "+2348123456789",
        "checkoutToken": "CkTkn_65faa63e-cc95-41bb-812e-1c1d921df70b"
    }

    result = Sms(header).CreatePremiumSubscription(body)
    print(result)

Delete Premium Subscription
---------------------------

To delete a premium subscription.

shortCode
^^^^^^^^^

This is the premium short code mapped to your account.

keyword
^^^^^^^

Your premium product keyword

phoneNumber
^^^^^^^^^^^

The phone number whose premium subscription is to be removed.

.. code:: python3

    from atlabs.sms import Sms

    header = {
        "base_url": "https://sandboxapi.fsi.ng",
        "Sandbox-Key": "your-sandbox-key-here",
        "Content-Type": "application/json"
    }

    body = {
        "shortCode": "19171",
        "keyword": "innovation-sandbox",
        "phoneNumber": "+2348123456789"
    }

    result = Sms(header).DeletePremiumSubscription(body)
    print(result)

Fetch Premium Subscription
--------------------------

Fetch your premium subscription data

shortCode
^^^^^^^^^

This is the premium short code mapped to your account.

keyword
^^^^^^^

A premium keyword under the above short code and mapped to your account.

lastReceivedId
^^^^^^^^^^^^^^

This is the id of the message that you last processed. Defaults to 0

.. code:: python3

    from atlabs.sms import Sms

    header = {
        "base_url": "https://sandboxapi.fsi.ng",
        "Sandbox-Key": "your-sandbox-key-here",
        "Content-Type": "application/json"
    }

    body = {
        "shortCode": "19171",
        "keyword": "innovation-sandbox",
        "lastReceivedId": "0"
    }

    result = Sms(header).FetchPremiumSubscription(body)
    print(result)

Fetch Message
-------------

Manually retrieve your messages

lastReceivedId
^^^^^^^^^^^^^^

This is the id of the message that you last processed. Defaults to 0

.. code:: python3

    from atlabs.sms import Sms

    header = {
        "base_url": "https://sandboxapi.fsi.ng",
        "Sandbox-Key": "your-sandbox-key-here",
        "Content-Type": "application/json"
    }

    body = {
        "lastReceivedId": "0"
    }

    result = Sms(header).FetchMessage(body)
    print(result)

Send Airtime
------------

You can send Send airtime to a bunch of phone numbers.

phoneNumber
^^^^^^^^^^^

Recipient of airtime.

currencyCode
^^^^^^^^^^^^

3-digit ISO format currency code.

amount
^^^^^^

Amount to charge.

.. code:: python3

    from atlabs.airtime import Airtime

    header = {
        "base_url": "https://sandboxapi.fsi.ng",
        "Sandbox-Key": "your-sandbox-key-here",
        "Content-Type": "application/json"
    }

    body = {
        "recipients": [{"phoneNumber": "+2349091271976", "amount": "1000", "currencyCode": "NGN"}]
    }

    result = Airtime(header).SendAirtime(body)
    print(result)

