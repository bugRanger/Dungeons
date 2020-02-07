from gameunit import GameUnit
from unitrace import UnitRace

class Gnoll(GameUnit):
	def __init__(self, name : str =''):
		super().__init__(name, UnitRace.Gnoll)
		