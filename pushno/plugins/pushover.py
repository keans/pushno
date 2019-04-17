import logging
from .baseplugin import AbstractClient
from pushno.messages.pushovermessages import PushOverValidationMessage


# API endpoint base URL
BASE_URL = "https://api.pushover.net/1"

# API endpoint to send messages
MESSAGE_URL = "{}/messages.json".format(BASE_URL)

# API endpoint to validate the user key
VALIDATE_URL = "{}/users/validate.json".format(BASE_URL)


# get the logger
log = logging.getLogger(__name__)


class PushOverClient(AbstractClient):
    def __init__(self, token, user):
        AbstractClient.__init__(self)
        self._token = token
        self._user = user

    def send(self, message):
        # override token and user in the given message
        message.token = self._token
        message.user = self._user

        log.debug("prepared message: {}".format(message.data))

        # ensure that message is correct
        message.validate()

        # finally, send the message
        r = self._s.post(MESSAGE_URL, data=message.data)
        res = r.json()

        log.debug("response: {}".format(res))

        return res["status"] == 1, res

    def validate_user(self, device=None):
        # prepare validation message
        validation_message = PushOverValidationMessage(
            token=self._token, user=self._user, device=device
        )

        log.debug("prepared message: {}".format(validation_message.data))

        # ensure that message is correct
        validation_message.validate()

        # get validation
        r = self._s.post(VALIDATE_URL, data=validation_message.data)
        res = r.json()

        log.debug("response: {}".format(res))

        return res["status"] == 1, res
