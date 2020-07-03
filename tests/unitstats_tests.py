import unittest

from common.unitstats import UnitStat
from common.unitstats import UnitStats
from common.unitstats import Health
from common.unitstats import Damage
from common.unitstats import CritRate
from common.unitstats import Level

class UnitStatsTest(unittest.TestCase):
	# Start test
	def setUp(self):
		self.__stat = UnitStat(10)
		self.__count = 0
		
	# Methods
	def test_stat_improve10_after_max1_equal_max(self):
		# Arrage
		max = 1
		self.__stat.Max = max
		# Act
		self.__stat.Improve(10)
		# Assert
		self.assertEqual(self.__stat.Value, max)
		
	def test_stat_max30_after_improve10_equal_value(self):
		# Arrage
		self.test_stat_improve10_after_max1_equal_max()
		max = 30
		# Act
		self.__stat.Max = max
		# Assert
		self.assertEqual(self.__stat.Value, 20)
		self.assertNotEqual(self.__stat.Value, max)
		
	def test_stat_improve10_after_min30_equal_min(self):
		# Arrage
		min = 30
		self.__stat.Min = min
		# Act
		self.__stat.Improve(10)
		# Assert
		self.assertEqual(self.__stat.Value, min)
		
	def test_stat_min30_after_improve20_equal_value(self):
		# Arrage
		min = 1
		self.test_stat_improve10_after_min30_equal_min()
		# Act
		self.__stat.Improve(20)
		# Assert
		self.assertEqual(self.__stat.Value, 40)
		self.assertNotEqual(self.__stat.Value, min)
		
	# TODO добавить тесты с маской.
	def test_stat_iadd10_equal_value20(self):
		# Arrage
		n = UnitStat(10)
		# Act
		self.__stat += n
		# Assert
		self.assertEqual(self.__stat.Value, 20)
	
	# TODO добавить тесты с маской.
	def test_stat_isub10_equal_value0(self):
		# Arrage
		n = UnitStat(10)
		# Act
		self.__stat -= n
		# Assert
		self.assertEqual(self.__stat.Value, 0)

	def __onIncCounter__(self, value):
		self.__count += value

	def test_stat_improve(self):
		# Arrage
		self.__count = 0
		self.__stat.Improved = self.__onIncCounter__
		# Act
		self.__stat.Improve(1)
		# Assert
		self.assertEqual(self.__stat.Value, 11)
		self.assertEqual(self.__count, 1)
		
	def test_stat_update(self):
		# Arrage
		self.__count = 0
		self.__stat.Updated = self.__onIncCounter__
		# Act
		self.__stat.Value += 1
		# Assert
		self.assertEqual(self.__stat.Value, 11)
		self.assertEqual(self.__count, 11)

	'''
		Health
	'''
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
		
	'''
		Damage
	'''
	def test_damage_min_value(self):
		# Arrage
		min = 1
		stat = Damage(10)
		# Act
		stat.Improve(-20)
		# Assert
		self.assertEqual(stat.Value, min)
		
	'''
		CritRate
	'''
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
		
	'''
		Level
	'''
	def test_level_max_value(self):
		# Arrage
		max = 5
		stat = Level(5)
		# Act
		stat.Improve(max*2)
		# Assert
		self.assertEqual(stat.Value, max)
	
	def test_level_min_value(self):
		# Arrage
		min = 1
		stat = Level(5)
		# Act
		stat.Improve(-20)
		# Assert
		self.assertEqual(stat.Value, min)
		
	'''
		UnitStats
	'''
	def test_unitstats_upgrade(self):
		# Arrage
		stats = UnitStats()
		# Act
		stats.Level.Value = 2
		# Assert
		self.assertEqual(stats.Level.Value, 2)
		self.assertEqual(stats.Experience.Max, 8)
		
	'''
		Experience
	'''
	def test_exp_upper_level(self):
		# Arrage
		stats = UnitStats()
		# Act
		stats.Experience.Improve(4)
		# Assert
		self.assertEqual(stats.Experience.Value, 4)
		self.assertEqual(stats.Experience.Max, 8)
		self.assertEqual(stats.Level.Value, 2)

if __name__ == '__main__':
	unittest.main()