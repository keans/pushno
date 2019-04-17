#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
