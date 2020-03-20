import unittest

from common.unitstats import UnitStat, Health, Damage, CritRate

class UnitStatsTest(unittest.TestCase):
	# Methods
	def test_stat_max_value(self):
		# Arrage
		max = 1
		stat = UnitStat(10)
		stat.Max = max
		# Act
		stat.Improve(10)
		# Assert
		self.assertEqual(stat.Value, max)
		
	def test_stat_min_value(self):
		# Arrage
		min = 1
		stat = UnitStat(10)
		stat.Min = min
		# Act
		stat.Improve(-10)
		# Assert
		self.assertEqual(stat.Value, min)

	def test_health_max_value(self):
		# Arrage
		max = 10
		stat = Health(max)
		# Act
		stat.Improve(20)
		# Assert
		self.assertEqual(stat.Value, max)

	def test_health_min_value(self):
		# Arrage
		min = 0
		stat = Health(10)
		# Act
		stat.Improve(-20)
		# Assert
		self.assertEqual(stat.Value, min)

	def test_health_new_value(self):
		# Arrage
		value = 5
		stat = Health(10)
		# Act
		stat.Value = value
		# Assert
		self.assertEqual(stat.Value, value)
		self.assertEqual(stat.Max, value)

	def test_damage_min_value(self):
		# Arrage
		min = 1
		stat = Damage(10)
		# Act
		stat.Improve(-20)
		# Assert
		self.assertEqual(stat.Value, min)

	def test_critrate_max_value(self):
		# Arrage
		max = 100
		stat = CritRate(10)
		# Act
		stat.Improve(max*2)
		# Assert
		self.assertEqual(stat.Value, max)
	
	def test_critrate_min_value(self):
		# Arrage
		min = 0
		stat = CritRate(10)
		# Act
		stat.Improve(-20)
		# Assert
		self.assertEqual(stat.Value, min)
	
if __name__ == '__main__':
	unittest.main()