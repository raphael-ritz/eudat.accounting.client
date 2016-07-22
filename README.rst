=======================
eudat.accounting.client
=======================

Upload accounting records to an eudat accounting server

Administrators of (storage) resources provided through the EUDAT Common Data 
Infrastructure can use this tool to conveniently report current resource 
consumption per registered resource. Accounting records are submitted per
individual resource identified by its (P)ID which is available as soon as
the resource has been registered at https://dp.eudat.eu

Default settings are such that only the resource id and the consumed value 
need to be provided. The default unit is ``byte`` and the default resource 
type is set to ``storage``.
The full documentation of options supported is described in the next section.


Full documentation and API
==========================

Installation
------------

The easiest way to install the tool is via ``pip`` or ``easy_install``.
It is usually best to do this in a ``virtualenv``:

.. code:: console

  $ pip install eudat.accounting.client

Command line interface
----------------------

As a result of the above there is now a console script called ``addRecord``.
Invoke it with ``-h`` to see its usage pattern and options:

.. code:: console

  $ bin/addRecord -h
  usage: addRecord [-h] [--version] [-b BASE_URL] [-u USER] [-p PASSWORD]
                   [-d DOMAIN] [-k KEY] [-t TYPE] [-n NUMBER] [-m MEASURE_TIME]
                   [-c COMMENT] [-v]
                   account value [unit]

  positional arguments:
    account               account to be used. Typically the (P)ID of the
                          resource to be accounted
    value                 The value to be recorded
    unit                  The unit of measurement for the value provided.
                          Default: "byte"

  optional arguments:
    -h, --help            show this help message and exit
    --version             show program's version number and exit
    -b BASE_URL, --base_url BASE_URL
                          base URL of the accounting server to use. Default:
                          https://accnt.eudat.eu
    -u USER, --user USER  user id used for logging into the server. If not
                          provided it is looked up in the environment variable
                          "ACCOUNTING_USER". Default: "" - aka not set
    -p PASSWORD, --password PASSWORD
                          password used for logging into the server. If not
                          provided it is looked up in the environment variable
                          "ACCOUNTING_PW". Default: "" - aka not set
    -d DOMAIN, --domain DOMAIN
                          name of the domain holding the account. Default: eudat
    -k KEY, --key KEY     key used to refer to the record. If not set the
                          accounting server will create the key. Specifying an
                          existing key will overwrite the existing record.
                          Default: "" - not set
    -t TYPE, --type TYPE  type of the resource accounted. Default: storage
    -s SERVICE, --service SERVICE
                          UID (or PID) of the registered service component
                          reporting the record. Default: "" - not set
    -n NUMBER, --number NUMBER
                          number of objects associated with this accounting
                          record. This is EUDAT specific. Default: "" - not set
    -o OBJECT_TYPE, --object_type OBJECT_TYPE
                          object type for the number of objects specified with
                          "-n". This is EUDAT specific. 
                          Default: "registered objects"
    -m MEASURE_TIME, --measure_time MEASURE_TIME
                          measurement time of the accounting record if different
                          from the current time. Default: "" - not set
    -c COMMENT, --comment COMMENT
                          arbitrary comment (goes into the meta dictionary).
                          Default: "" - not set
    -v, --verbose         return the key of the accounting record created.
                          Default: off


Most of this should be self-explaining. Note that you need to provide credentails
for the accounting service. If you do not have any contact the EUDAT accounting 
manager.

Basic usage information as well as error messages are logged to a file named
``.accounting.log`` in the current working directory from where ``addRecord``
has been invoked.


Developer notes
===============

Please use a ``virtualenv`` to maintain this package, but I should not need to say that.

The package can be installed directly from GitHub:

.. code:: console

  $ pip install git+git://github.com/EUDAT-DPMT/eudat.accounting.client

The code is organized in a nested namespace package, i.e., the real action
is happening in the subdirectory 

.. code:: console

  $ cd src/eudat/accounting/client
  
Start looking around there.

Run the tests (not really that meaningful so far):

.. code:: console

  $ python setup.py test
  $ python run_tests.py


Links
=====

Project home page

  https://github.com/EUDAT-DPMT/eudat.accounting.client

Source code

  https://github.com/EUDAT-DPMT/eudat.accounting.client

Issues tracker

  https://github.com/EUDAT-DPMT/eudat.accounting.client/issues
