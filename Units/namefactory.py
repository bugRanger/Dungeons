from abc import ABC, abstractmethod
from namegenerator import NameGenerator
from gnollnames import GnollNames

class NameFactory(ABC):
    def __init__(self, generator : NameGenerator):
        self.__generator = generator

    def MakeName(self) -> str:
        return self.__generator.GetRandom()

class ConcreateGnollName(NameFactory):
    def __init__(self):
        super().__init__(GnollNames())
