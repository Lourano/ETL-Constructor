import random
import string

from ..structure import Extractor


class SimpleExtractor(Extractor):
    def __init__(self, parameters):
        self.parameters = parameters

    def extract(self):
        print("Extracting...")
        return random.choices(population=list(
            set(string.ascii_lowercase).union(
                set(string.ascii_uppercase)
            )
        ),
            k=self.parameters['k']
        )
