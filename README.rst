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

    python setup.py install


Basic Setup
-----------

In the first step, you need to setup an account at
`PushOver <https://pushover.net/>`_ or `Prowl <https://www.prowlapp.com>`_
and create a corresponding API key that you want to use.


Examples
--------

The easiest way to send a push message with ``pushno`` is to use the
``PushNotification`` class that provides a common interface to all available
push notification services.


Prowl
^^^^^

For Prowl do:

::

    from pushno import PushNotification

    PUSHNO_PROWL_API_KEY = "<your_prowl_api_key>"

    pn = PushNotification(
        "prowl", api_key=PUSHNO_PROWL_API_KEY, application="pushno"
    )
    is_valid, res = pn.validate_user()
    if is_valid:
        pn.send(event="How simple is that?", description="Great News")
    else:
        print(res)


PushOver
^^^^^^^^

For PushOver do:

::

    from pushno import PushNotification

    PUSHNO_PUSHOVER_API_KEY = "<your_pushover_api_key>"
    PUSHNO_PUSHOVER_USER_KEY = "<your_pushover_user_key>"

    pn = PushNotification(
        "pushover", token=PUSHNO_PUSHOVER_API_KEY,
        user=PUSHNO_PUSHOVER_USER_KEY
    )
    is_valid, res = pn.validate_user()
    if is_valid:
        pn.send(title="How simple is that?", message="Great News")
    else:
        print(res)

Note that the validation part is optional, so if you are sure that the API key
is working as expected, you can send the push message directly. As a result,
you can send a push message in two lines of code. The API key is the
key of the specific app.


It is also possible to use the underlying client classes directly, which
is however a little bit more verbose:

Prowl
^^^^^

::

    from pushno.plugins import ProwlClient
    from pushno.messages import ProwlMessage

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



PushOver
^^^^^^^^

::

    from pushno.plugins import PushOverClient
    from pushno.messages import PushOverMessage

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
        print(res["errors"])

Again the validation part of the user's API key is optional.


For the complete example scripts see https://github.com/keans/pushno/tree/master/examples .


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
