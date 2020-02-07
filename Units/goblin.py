from gameunit import GameUnit
from unitrace import UnitRace

class Goblin(GameUnit):
	def __init__(self, name : str =''):
		super().__init__(name, UnitRace.Goblin)
		