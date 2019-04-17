from abc import ABC, abstractmethod

import requests


class AbstractClient(ABC):
    def __init__(self, api_key="", user_key=""):
        self._api_key = api_key
        self._user_key = user_key
        self._s = requests.Session()

    @abstractmethod
    def send(self, message):
        pass
