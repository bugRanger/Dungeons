from abc import ABC, abstractmethod

class NameGenerator(ABC):
    @abstractmethod
    def GetName(self) -> str:
        pass