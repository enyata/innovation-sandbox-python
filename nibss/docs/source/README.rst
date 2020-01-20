
Innovation Sandbox (nibss)
============

| A Python module that gives access to the innovation sandbox API on the go!

Features
~~~~~~~~

* Super easy to use
* A very easy to understand
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

*  to reset bvn credentials

.. code:: python

    >>> from nibss.request import Request
    >>> header = {
      "Organizationcode": "11111",
      "sandbox-key": "0ae0db703c04119b3db7a03d7f854c13",
      "content-type" :"application/json",
      "accept": "application/json",
      "username": "11111",
      "password": "^o'e6EXK5T ~^j2="
      }
    >>> reset = Request(header).bvn_reset()
    >>> print(reset)
    >>> {'aes_key': '9+CZaWqfyI/fwezX', 'password': "^o'e6EXK5T ~^j2=", 'ivkey': 'eRpKTBjdOq6T67D0'}


* To get the code for function used