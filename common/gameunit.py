from abc import ABC, abstractmethod

from common.uid import Uid
from common.enums.unitrace import UnitRace
from common.unitstrategy import UnitStrategy
from common.unitstats import UnitStats

class GameUnit:
	 # TODO Add UnitStats constructor param.
	 # Constructor
	def __init__(self, name : str, stats : UnitStats, race : UnitRace):
		self.__uid = Uid()
		self.__name = name
		self.__race = race
		self.__stats = stats
		self.__strategy = None
	
	# Property
	@property
	def Uid(self) -> Uid :
		return self.__uid

	@property
	def Name(self):
		return self.__name

	@property
	def Race(self) -> UnitRace :
		return self.__race

	@property
	def Stats(self) -> UnitStats:
		return self.__stats

	# Methods
	def IsAlive(self):
		return self.Stats.Health.Value > 0
	
	# Bot strategy
	def SetStrategy(self, value : UnitStrategy):
		self.__strategy = value

	@abstractmethod
	def Action(self):
		# TODO Оценить состояние по дизейблам.
		if self.Stats.Health.Value == 0:
			return
		self.__strategy.Action(self.Uid)

	# ToString
	def __str__(self):
		return "Uid: {}\n{}: {}\n{}".format(self.Uid, self.__race, self.Name, self.Stats)
		