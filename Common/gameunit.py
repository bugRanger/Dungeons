from gameobject import GameObject
from unitrace import UnitRace

class GameUnit(GameObject):	
	 # Constructor
	def __init__(self, name : str, type : UnitRace):
		self.__type=type
		super().__init__(name)
	
	# Property
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