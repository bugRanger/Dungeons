from common.gameunit import GameUnit
from common.unitstats import UnitStats
from common.enums.unitrace import UnitRace

class Gnoll(GameUnit):
	def __init__(self, name : str, desc: str, stats: UnitStats):
		super().__init__(name, desc, stats, UnitRace.Gnoll)
	# TODO Add specific behaviors