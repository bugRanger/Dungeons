
class UnitStats:
	# TODO Add stats:
	# % crit, hit, dodge and others
	def UnitStats(self, basic: UnitStats = None):
		self.__basic = basic
	
	'''
	Negative and positive stats/buffs.
	Current unit stats cannot be negative after update.
	'''
	# Add stats
	def Update(self, stats: UnitStats):
		pass
		
	# Basic stats
	def Basic(self) -> UnitStats:
		return self.__basic