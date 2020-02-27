from abc import ABC, abstractmethod

from common.combatsession import CombatSession
from common.unitstrategy import UnitStrategy

from unit.meleestrategy import MeleeStrategy

class StrategyFactory(ABC):
	@abstractmethod
	def Create(self, session : CombatSession):
		pass
		
	def Make(self, session : CombatSession) -> UnitStrategy:
		return self.Create(session)
		
class ConcreateMeleeStrategy(StrategyFactory):
	def Create(self, session: CombatSession) -> MeleeStrategy:
		return MeleeStrategy(session)