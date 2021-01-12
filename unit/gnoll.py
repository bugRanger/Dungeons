from common.gameunit import GameUnit
from common.unitstats import UnitStats
from common.enums.unitrace import UnitRace

class GnollStats(UnitStats):
	def __init__(self):
		super().__init__()

	def UpdateLevel(self, value):
		super().UpdateLevel(value)
		self.Health.Value = value * 5
		self.Damage.Value = value + 1

class Gnoll(GameUnit):
	def __init__(self, name : str, stats: UnitStats = None):
		super().__init__(name, stats if stats is not None else GnollStats(), UnitRace.Gnoll)
	# TODO Add specific behaviors