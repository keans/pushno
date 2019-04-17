from pushno.consts.pushoverconsts import LOWEST_PRIORITY, LOW_PRIORITY, \
    NORMAL_PRIORITY, HIGH_PRIORIRY, EMERGENCY_PRIORITY, \
    PUSHOVER_SOUND, BIKE_SOUND, BUGLE_SOUND, \
    CASHREGISTER_SOUND, CLASSICAL_SOUND, COSMIC_SOUND, \
    FALLING_SOUND, GAMELAN_SOUND, INCOMING_SOUND, \
    INTERMISSION_SOUND, MAGIC_SOUND, MECHANICAL_SOUND, \
    PIANOBAR_SOUND, SIREN_SOUND, SPACEALARM_SOUND, \
    TUGBOAT_SOUND, ALIEN_SOUND, CLIMB_SOUND, \
    PERSISTENT_SOUND, ECHO_SOUND, UPDOWN_SOUND, NONE_SOUND


# schema for PushOver message
pushover_message_schema = {
    # ----- required -----
    "token": {
        "type": "string",
        "required": True,
        "empty": False,
        "minlength": 30,
        "maxlength": 30,
        "regex": r"^[A-Za-z0-9]+$"
    },
    "user": {
        "type": "string",
        "required": True,
        "empty": False,
        "minlength": 30,
        "maxlength": 30,
        "regex": r"^[A-Za-z0-9]+$"
    },
    "message": {
        "type": "string",
        "required": True,
        "empty": False,
        "minlength": 1,
        "maxlength": 1024,
    },
    # ----- optional -----
    "attachment": {
        # TODO: needs improved checking
        "type": "string",
        "required": False,
        "empty": False,
    },
    "device": {
        "type": "string",
        "required": False,
        "empty": False,
        "minlength": 1,
        "maxlength": 25,
        "regex": r"^[A-Za-z0-9_-]+$"
    },
    "title": {
        "type": "string",
        "required": False,
        "empty": False,
        "minlength": 1,
        "maxlength": 250,
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
    "url_title": {
        "type": "string",
        "required": False,
        "empty": False,
        "minlength": 1,
        "maxlength": 100,
    },
    "priority": {
        "type": "string",
        "required": False,
        "empty": False,
        "allowed": [
            LOWEST_PRIORITY, LOW_PRIORITY, NORMAL_PRIORITY,
            HIGH_PRIORIRY, EMERGENCY_PRIORITY
        ]
    },
    "sound": {
        "type": "string",
        "required": False,
        "empty": False,
        "allowed": [
            PUSHOVER_SOUND, BIKE_SOUND, BUGLE_SOUND,
            CASHREGISTER_SOUND, CLASSICAL_SOUND, COSMIC_SOUND,
            FALLING_SOUND, GAMELAN_SOUND, INCOMING_SOUND,
            INTERMISSION_SOUND, MAGIC_SOUND, MECHANICAL_SOUND,
            PIANOBAR_SOUND, SIREN_SOUND, SPACEALARM_SOUND,
            TUGBOAT_SOUND, ALIEN_SOUND, CLIMB_SOUND,
            PERSISTENT_SOUND, ECHO_SOUND, UPDOWN_SOUND, NONE_SOUND
        ]
    },
}


# schema for PushOver message
pushover_validation_message_schema = {
    # ----- required -----
    "token": {
        "type": "string",
        "required": True,
        "empty": False,
        "minlength": 30,
        "maxlength": 30,
        "regex": r"^[A-Za-z0-9]+$"
    },
    "user": {
        "type": "string",
        "required": True,
        "empty": False,
        "minlength": 30,
        "maxlength": 30,
        "regex": r"^[A-Za-z0-9]+$"
    },
    # ----- optional -----
    "device": {
        "type": "string",
        "required": False,
        "empty": False,
        "minlength": 1,
        "maxlength": 25,
        "regex": r"^[A-Za-z0-9_-]+$"
    },
}
