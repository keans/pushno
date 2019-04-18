from abc import ABC, abstractmethod

import requests


class AbstractClient(ABC):
    def __init__(self, **kwargs):
        self._s = requests.Session()

    @abstractmethod
    def send(self, message):
        pass

    @abstractmethod
    def validate_user(self, **kwargs):
        pass
