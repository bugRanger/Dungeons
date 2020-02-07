from gameobject import GameObject
from unitrace import UnitRace

class GameUnit(GameObject):
	__health : int = 1
	__damage : int = 1
	__type : UnitRace = None
	
	 # Constructor
	def __init__(self, name : str, type : UnitRace):
		self.__type=type
		self.__name=name
	 
	@property
	def Health(self) -> int:
		return self.__health
		
	@Health.setter
	def Health(self, value):
		self.__health = value

	@property
	def Damage(self) -> int:
		return self.__damage

	def IsAlive(self):
		return self.__health > 0