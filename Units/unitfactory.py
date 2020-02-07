from abc import ABC, abstractmethod
from goblin import Goblin
from gameunit import GameUnit

class UnitCreator(ABC):
	@abstractmethod
	def CreateUnit(self, name : str = ''):
		pass
		
	def Make(self, name : str = '') -> GameUnit:
		return self.CreateUnit(name)

class ConcreateGoblin(UnitCreator):
	def CreateUnit(self, name : str ='') -> Goblin:
		return Goblin(name)
		
#class Concreate__(UnitCreator):
#	def CreateUnit(self, name : str ='') -> __:
#		return __(name)