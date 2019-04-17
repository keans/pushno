from cerberus import Validator

from .basemessage import BaseMessage

from pushno.schemas.prowlschema import prowl_message_schema, \
    prowl_validation_message_schema


class ProwlMessage(BaseMessage):
    """
    a prowl message to send a push message
    """
    def __init__(self, **kwargs):
        BaseMessage.__init__(
            self, Validator(prowl_message_schema), **kwargs
        )


class ProwlValidationMessage(BaseMessage):
    """
    a prowl validation message to validate a user key
    """
    def __init__(self, **kwargs):
        BaseMessage.__init__(
            self, Validator(prowl_validation_message_schema), **kwargs
        )
