from pushno.exceptions import InvalidService

from pushno.plugins import PushOverClient, ProwlClient
from pushno.messages import PushOverMessage, ProwlMessage


class PushNotification:
    """
    helper class to ease the use of all provided services
    under a common class
    """
    def __init__(self, service_type, **kwargs):
        if service_type == "pushover":
            # --- pushover ---
            self._client = PushOverClient(**kwargs)
        elif service_type == "prowl":
            # --- prowl ---
            self._application = kwargs.pop("application", None)
            self._client = ProwlClient(**kwargs)
        else:
            raise InvalidService("Invalid service: '{}'".format(service_type))

    def send(self, **kwargs):
        """
        send a push message
        """
        if isinstance(self._client, PushOverClient):
            # --- pushover ---
            msg = PushOverMessage(**kwargs)
        elif isinstance(self._client, ProwlClient):
            # --- prowl ---
            if self._application is not None:
                # automatically add internally set application
                kwargs["application"] = self._application
            msg = ProwlMessage(**kwargs)

        # send the message using the underlying client
        return self._client.send(msg)

    def validate_user(self, device=None):
        """
        check if the provided user credentials are correct
        """
        # --- pushover ---
        if isinstance(self._client, PushOverClient):
            return self._client.validate_user(device=device)

        elif isinstance(self._client, ProwlClient):
            # --- prowl ---
            return self._client.validate_user()
