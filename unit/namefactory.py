from abc import ABC, abstractmethod
from random import randint
from common.gamedice import GameDice
from common.namegenerator import NameGenerator
from unit.gnollnames import GnollNames

class NameFactory(ABC):
    def __init__(self, generator : NameGenerator):
        self.__generator = generator

    def Make(self) -> str:
        return self.__generator.GetName()

class ConcreateGnollName(NameFactory):
    def __init__(self):
        super().__init__(GnollNames(GameDice.Drop))
