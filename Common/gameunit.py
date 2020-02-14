from abc import ABC, abstractmethod
from uid import Uid
from gameobject import GameObject
from unitrace import UnitRace
from unitaction import UnitAction
from unitstrategy import UnitStrategy
from combatsession import CombatSession

class GameUnit(GameObject):
	 # Constructor
	def __init__(self, name : str,  desc : str, health: int, damage: int, type : UnitRace):
		self.__uid = Uid()
		self.__type = type
		self.__health = health
		self.__damage = damage
		self.__strategy = None
		super().__init__(name, desc)
	
	# Property
	@property
	def Uid(self) -> Uid :
		return self.__uid
	
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
		
	def SetStrategy(self, value : UnitStrategy):
		self.__strategy = value
			
	def Action(self) -> UnitAction:
		return self.__strategy.Action(self.Uid)

	# To string
	def __str__(self):
		return "{0}: {1}\nHealth: {2}\nDamage: {3}".format(self.__type, self.Name, self.__health, self.__damage)
		