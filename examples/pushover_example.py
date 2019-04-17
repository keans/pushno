#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
    print(res["errors"])
