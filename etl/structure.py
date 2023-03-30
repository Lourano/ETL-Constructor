from abc import ABC, abstractmethod


class Extractor(ABC):

    @abstractmethod
    def extract(self):
        pass


class Loader(ABC):

    @abstractmethod
    def load(self, data):
        pass


class ETL(ABC):
    def __init__(self, extractor, loader):
        self.extractor: Extractor = extractor
        self.loader: Loader = loader

    def extract(self):
        return self.extractor.extract()

    @abstractmethod
    def transform(self, data):
        pass

    def load(self, data):
        return self.loader.load(data=data)

    def run(self):
        data = self.extract()
        transformed = self.transform(data=data)
        self.load(data=transformed)

