==================
BVN Reset
==================

A place to reset BVN credentials

* To see all the available functions in a module, you can just type ``help()`` with the module name as argument. For example,
.. code-block:: python

    # import Request
   >>> from nibss.request import Request
   >>> help(reset)

    # to reset bvn credentials

   Request({
      "Organizationcode": "11111",
      "sandbox-key": "0ae0db703c04119b3db7a03d7f854c13",
      "content-type" :"application/json",
      "accept": "application/json",
      "username": "11111",
      "password": "^o'e6EXK5T ~^j2="
      }).bvn_reset()

* The Request object takes all the parameters for the header as a dictionary
