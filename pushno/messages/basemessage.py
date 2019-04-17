from abc import ABC

from ..exceptions import InvalidParamType, InvalidParamValue


class BaseMessage(ABC):
    """
    base message class from which the different message
    classes of the different provider must be derived
    """

    def __init__(self, validator, **kwargs):
        # validator later on used for checking the message
        self._validator = validator

        self._values = {}

        # ensure that only available parameters are passed
        for k in kwargs.keys():
            if k not in self.all_params:
                raise InvalidParamType(
                    "Invalid parameter '{}' for {}".format(
                        k, self.__class__.__name__
                    )
                )
            else:
                # store internal value for message field
                if kwargs[k] is not None:
                    self._values[k] = kwargs[k]

    def __getattr__(self, key):
        """
        override getattr to return message specific field values
        """
        print(key)
        if not key.startswith("_") and key in self._values.keys():
            return self._values[key]

        raise AttributeError()

    def __setattr__(self, key, value):
        """
        override setattr to return message specific field values
        """
        if key.startswith("_"):
            # set normal attribute
            super(BaseMessage, self).__setattr__(key, value)
        elif key in self.all_params:
            # set one of the message parameters
            self._values[key] = value
        else:
            # unknown parameter
            raise AttributeError()

    @property
    def all_params(self):
        """
        return the names of all valid parameters
        """
        return list(self._validator.schema.keys())

    @property
    def required_params(self):
        """
        return the names of all required parameters
        """
        return [
            k
            for k in self.all_params
            if self._validator.schema[k]["required"] is True
        ]

    @property
    def optional_params(self):
        """
        return the names of all optional parameters
        """
        return [
            k
            for k in self.all_params
            if self._validator.schema[k]["required"] is False
        ]

    @property
    def data(self):
        """
        returns the message representation as dictionary
        """
        return self._values

    def validate(self):
        """
        validate the message using the set validator
        and raise an exception if the validator fails
        """
        if self._validator.validate(self.data) is False:
            raise InvalidParamValue(self._validator.errors)
