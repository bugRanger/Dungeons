from abc import ABC, abstractmethod
from gnoll import Gnoll
from gameunit import GameUnit

class UnitCreator(ABC):
	@abstractmethod
	def CreateUnit(self, name : str = ''):
		pass

	def MakeUnit(self, name : str = '') -> GameUnit:
		return self.CreateUnit(name)

class ConcreateGnoll(UnitCreator):
	def CreateUnit(self, name : str ='') -> Gnoll:
		return Gnoll(name)
		
#class Concreate__(UnitCreator):
#	def CreateUnit(self, name : str ='') -> __:
#		return __(name)