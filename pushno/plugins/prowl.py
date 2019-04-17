import logging
import xml.etree.ElementTree as ET

from .baseplugin import AbstractClient

from pushno.messages import ProwlValidationMessage


# API endpoint base URL
BASE_URL = "https://api.prowlapp.com/publicapi"

# API endpoint to send messages
MESSAGE_URL = "{}/add".format(BASE_URL)

# API endpoint to validate the user key
VALIDATE_URL = "{}/verify".format(BASE_URL)


# get the logger
log = logging.getLogger(__name__)


class ProwlClient(AbstractClient):
    def __init__(self, api_key, provider_key=None):
        AbstractClient.__init__(self)
        self._api_key = api_key
        self._provider_key = provider_key

    def _parse_result(self, r):
        root = ET.fromstring(r.text).getchildren()[0]
        d = root.attrib
        if root.text is not None:
            d["status"] = root.text

        return d

    def send(self, message):
        # override token and user in the given message
        message.apikey = self._api_key
        if self._provider_key is not None:
            message.providerkey = self._provider_key

        log.debug("prepared message: {}".format(message.data))

        # ensure that message is correct
        message.validate()

        # finally, send the message
        r = self._s.post(MESSAGE_URL, data=message.data)
        res = self._parse_result(r)

        log.debug("response: {}".format(res))

        return res["code"] == "200", res

    def validate_user(self, device=None):
        # prepare validation message
        validation_message = ProwlValidationMessage(
            apikey=self._api_key, providerkey=self._provider_key
        )

        log.debug("prepared message: {}".format(validation_message.data))

        # ensure that message is correct
        validation_message.validate()

        # get validation
        r = self._s.get(VALIDATE_URL, params=validation_message.data)
        res = self._parse_result(r)

        log.debug("response: {}".format(res))

        return res["code"] == "200", res
