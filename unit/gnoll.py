from common.gameunit import GameUnit
from common.enums.unitrace import UnitRace

class Gnoll(GameUnit):
	def __init__(self, name : str, desc: str, health: int, damage: int):
		super().__init__(name, desc, health, damage, UnitRace.Gnoll)
	# TODO Add specific behaviors