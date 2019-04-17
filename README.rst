pushno
======

``pushno`` is a Python package for sending push notifications to mobile
devices. It provides a simple, common interface for sending push notifications
via the two services `PushOver <https://pushover.net/>`_ and `Prowl
<https://www.prowlapp.com>`_.

``pushno`` focuses on Python 3.x so there will be no legacy support for Python 2.x. Due to its modular structure theoretically further services can
be added.


Module Installation
-------------------

The easiest way to install the newest version of the ``pushno``
module is via ``pip``:


::

    pip install -U pushno

or clone/download this repository and install it:

::

    python3 setup.py install

or

::

    python setup.py install


Basic Setup
-----------

In the first step, you need to setup an account at
`PushOver <https://pushover.net/>`_ or `Prowl <https://www.prowlapp.com>`_
and create a corresponding API key that you want to use.


Examples
--------

In the following for each service a short example is discussed:

Prowl
^^^^^

The easiest way to send a message via Prowl is shown in the following:

::

    import os

    from pushno.plugins import ProwlClient
    from pushno.messages import ProwlMessage

    # get api key and user key from environment variables
    PUSHNO_PROWL_API_KEY = os.getenv("PUSHNO_PROWL_API_KEY")

    # prepare the pushover client
    client = ProwlClient(PUSHNO_PROWL_API_KEY)

    # validate the user key
    is_valid, res = client.validate_user()
    if is_valid is True:
        # key is still valid => send a notification message
        res = client.send(
            ProwlMessage(
                application="pushno",
                event="How simple is that?",
                description="Great News"
            )
        )
        print(res)

    else:
        print(res)


The validation of the user is optional, so if you are sure that the API key
is working as expected, you can send the message directly.

PushOver
^^^^^^^^

Similarly, a message can be sent using PushOver as shown in the following:

::

    import os

    from pushno.plugins import PushOverClient
    from pushno.messages import PushOverMessage

    # get api key and user key from environment variables
    PUSHNO_PUSHOVER_API_KEY = os.getenv("PUSHNO_PUSHOVER_API_KEY")
    PUSHNO_PUSHOVER_USER_KEY = os.getenv("PUSHNO_PUSHOVER_USER_KEY")

    # prepare the pushover client
    client = PushOverClient(PUSHNO_PUSHOVER_API_KEY, PUSHNO_PUSHOVER_USER_KEY)

    # validate the user key
    is_valid, res = client.validate_user()
    if is_valid is True:
        # key is still valid => send a notification message
        client.send(
            PushOverMessage(
                title="Great News",
                message="How simple is that?"
            )
        )

    else:
        print(res["error"])

Again the validation part of the user's API key is optional.


For more example scripts see https://github.com/keans/pushno/tree/master/examples .


Development
-----------

If you want to contribute in the development, please check out the source code
at https://github.com/keans/pushno.git .


To get started with the development:

::

    git clone git@github.com:keans/pushno.git
    cd pushno/
    python3 -m venv env
    source env/bin/activate
    pip install -r requirements.txt


For verbose debug output simply set the logging level to debug:

::

    import logging
    logging.basicConfig(level=logging.DEBUG)
