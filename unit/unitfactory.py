from abc import ABC, abstractmethod

from common.gameunit import GameUnit
from common.unitstats import UnitStats
from unit.gnoll import Gnoll

class UnitCreator(ABC):
	@abstractmethod
	def Create(self, name : str):
		pass

	def Make(self, name : str) -> GameUnit:
		return self.Create(name)

class ConcreateGnoll(UnitCreator):
	# TODO Add support basic stats for race/unit.
	def Create(self, name : str) -> Gnoll:
		stats = UnitStats()
		stats.Health.Value = 12
		stats.Damage.Value = 2
		return Gnoll(name, '', stats)
		
#class Concreate__(UnitCreator):
#	def CreateUnit(self, name : str ='') -> __:
#		return __(name)