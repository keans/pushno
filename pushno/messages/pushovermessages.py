from cerberus import Validator

from .basemessage import BaseMessage

from pushno.schemas.pushoverschema import pushover_message_schema, \
    pushover_validation_message_schema


class PushOverMessage(BaseMessage):
    """
    a PushOver message to send a push message
    """
    def __init__(self, **kwargs):
        BaseMessage.__init__(
            self, Validator(pushover_message_schema), **kwargs
        )


class PushOverValidationMessage(BaseMessage):
    """
    a PushOver validation message to validate a user key
    """
    def __init__(self, **kwargs):
        BaseMessage.__init__(
            self, Validator(pushover_validation_message_schema), **kwargs
        )
