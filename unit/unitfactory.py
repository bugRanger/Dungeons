from abc import ABC, abstractmethod

from common.gameunit import GameUnit
from unit.gnoll import Gnoll

class UnitCreator(ABC):
	@abstractmethod
	def Create(self, name : str):
		pass

	def Make(self, name : str) -> GameUnit:
		return self.Create(name)

class ConcreateGnoll(UnitCreator):
	def Create(self, name : str) -> Gnoll:
		# TODO Table of unit hp/dmg.
		return Gnoll(name, '', 12, 2)
		
#class Concreate__(UnitCreator):
#	def CreateUnit(self, name : str ='') -> __:
#		return __(name)