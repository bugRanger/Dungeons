from abc import ABC, abstractmethod
from uid import Uid
from unitaction import UnitAction
from combatsession import CombatSession

class UnitStrategy(ABC):
	@abstractmethod
	def Action(self, unit : Uid) -> UnitAction:
		pass

class MeleeStrategy(UnitStrategy):
	def Action(self, unit : Uid) -> UnitAction:
		return UnitAction.Attack