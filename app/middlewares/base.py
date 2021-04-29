from abc import ABC, abstractmethod


class ThryveBaseMiddleware(ABC):
    def __init__(self, app):
        self.app = app

    def __call__(self):
        self._process()

    @abstractmethod
    def _process(self):
        pass

