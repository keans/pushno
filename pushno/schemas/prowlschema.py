from pushno.consts.prowlconsts import VERY_LOW_PRIORITY, MODERATE_PRIORITY, \
    NORMAL_PRIORITY, HIGH_PRIORIRY, EMERGENCY_PRIORITY


# schema for prowl message
prowl_message_schema = {
    # ----- required -----
    "apikey": {
        "type": "string",
        "required": True,
        "empty": False,
        "minlength": 40,
        "regex": r"^[A-Fa-f0-9,]+$"  # TODO: improve the list of keys
    },
    "application": {
        "type": "string",
        "required": True,
        "maxlength": 256,
    },
    "event": {
        "type": "string",
        "required": True,
        "empty": False,
        "minlength": 1,
        "maxlength": 1024,
    },
    "description": {
        "type": "string",
        "required": True,
        "empty": False,
        "minlength": 1,
        "maxlength": 10000,
    },

    # ----- optional -----
    "providerkey": {
        "type": "string",
        "required": False,
        "empty": False,
        "minlength": 40,
        "maxlength": 40,
        "regex": r"^[A-Za-z0-9]+$"
    },
    "priority": {
        "type": "string",
        "required": False,
        "empty": False,
        "allowed": [
            VERY_LOW_PRIORITY, MODERATE_PRIORITY, NORMAL_PRIORITY,
            HIGH_PRIORIRY, EMERGENCY_PRIORITY
        ]
    },
    "url": {
        "type": "string",
        "required": False,
        "empty": False,
        "minlength": 1,
        "maxlength": 512,
        "regex": (
            r"^[a-z]+://([^/:]+\.[a-z]{2,10}'|"
            r"([0-9]{1,3}\.){3}[0-9]{1,3})(:[0-9]+)?(\/.*)?$"
        )
    },
}


# schema for prowl message
prowl_validation_message_schema = {
    # ----- required -----
    "apikey": {
        "type": "string",
        "required": True,
        "empty": False,
        "minlength": 40,
        "regex": r"^[A-Fa-f0-9]+$"
    },
    # ----- optional -----
    "providerkey": {
        "type": "string",
        "required": False,
        "empty": False,
        "minlength": 40,
        "maxlength": 40,
        "regex": r"^[A-Za-z0-9]+$"
    },
}
