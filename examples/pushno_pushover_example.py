#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from pushno import PushNotification

# get api key and user key from environment variables
PUSHNO_PUSHOVER_API_KEY = os.getenv("PUSHNO_PUSHOVER_API_KEY")
PUSHNO_PUSHOVER_USER_KEY = os.getenv("PUSHNO_PUSHOVER_USER_KEY")

pn = PushNotification(
    "pushover", token=PUSHNO_PUSHOVER_API_KEY, user=PUSHNO_PUSHOVER_USER_KEY
)
is_valid, res = pn.validate_user()
if is_valid:
    pn.send(title="How simple is that?", message="Great News")
else:
    print(res)
