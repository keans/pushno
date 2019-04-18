#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from pushno import PushNotification

# get api key and user key from environment variables
PUSHNO_PROWL_API_KEY = os.getenv("PUSHNO_PROWL_API_KEY")

pn = PushNotification(
    "prowl", api_key=PUSHNO_PROWL_API_KEY, application="pushno"
)
is_valid, res = pn.validate_user()
if is_valid:
    pn.send(event="How simple is that?", description="Great News")
else:
    print(res)
