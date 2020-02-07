from abc import ABC, abstractmethod

class NameGenerator(ABC):
    @abstractmethod
    def GetRandom(self) -> str:
        pass