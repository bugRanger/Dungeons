from enum import Enum, auto

class UnitAction(Enum):
    Attack = auto()
    Cast = auto()
    Run = auto()
    Stop = auto()