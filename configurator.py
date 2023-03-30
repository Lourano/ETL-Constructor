from importlib import import_module

from etl.structure import (
    Extractor,
    Loader,
    ETL
)


class ETLConfigurator:
    def __init__(self, config):
        self.config = config
        self.module = import_module(self.config['module'])

    def extractor(self) -> Extractor:
        instance = getattr(self.module, self.config['extractor'])
        return instance(parameters=self.config['parameters'])

    def loader(self) -> Loader:
        instance = getattr(self.module, self.config['loader'])
        return instance(config=self.config['loader-config'])

    def etl(self) -> ETL:
        instance = getattr(self.module, self.config['ETL'])
        return instance(extractor=self.extractor(), loader=self.loader())
