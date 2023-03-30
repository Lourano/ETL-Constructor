from ..structure import Loader


class SimpleLoader(Loader):
    def __init__(self, config):
        self.config = config

    def load(self, data):
        print(f"{data}\nLoaded. Config: {self.config}")
