from abc import ABC, abstractmethod

from unitstrategy import UnitStrategy
from meleestrategy import MeleeStrategy
from combatsession import CombatSession

class StrategyFactory(ABC):
	@abstractmethod
	def Create(self, session : CombatSession):
		pass
		
	def Make(self, session : CombatSession) -> UnitStrategy:
		return self.Create(session)
		
class ConcreateMeleeStrategy(StrategyFactory):
	def Create(self, session: CombatSession) -> MeleeStrategy:
		return MeleeStrategy(session)