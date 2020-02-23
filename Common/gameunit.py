from abc import ABC, abstractmethod

from uid import Uid
from gameobject import GameObject
from unitrace import UnitRace
from unitstrategy import UnitStrategy

class GameUnit(GameObject):
	 # Constructor
	def __init__(self, name : str,  desc : str, health: int, damage: int, race : UnitRace):
		self.__uid = Uid()
		self.__race = race
		self.__health = health
		self.__damage = damage
		self.__strategy = None
		super().__init__(name, desc)
	
	# Property
	@property
	def Uid(self) -> Uid :
		return self.__uid
		
	@property
	def Race(self) -> UnitRace :
		return self.__race
		
	@property
	def Health(self) -> int:
		return self.__health
		
	@Health.setter
	def Health(self, value):
		self.__health = value

	@property
	def Damage(self) -> int:
		return self.__damage

	# Methods
	def IsAlive(self):
		return self.__health > 0
	
	# Bot strategy
	def SetStrategy(self, value : UnitStrategy):
		self.__strategy = value
		
	@abstractmethod		
	def Action(self):
		# TODO Оценить состояние по дизейблам.
		if self.Health == 0:
			return
		self.__strategy.Action(self.Uid)

	# ToString
	def __str__(self):
		return "Uid: {}\n{}: {}\nHealth: {}\nDamage: {}".format(self.Uid, self.__race, self.Name, self.__health, self.__damage)
		