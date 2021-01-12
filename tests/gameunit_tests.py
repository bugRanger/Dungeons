import unittest
from unittest.mock import patch

from common.gameunit import GameUnit, UnitRace
from common.unitstats import UnitStats

class GameUnitTests(unittest.TestCase):
	def setUp(self):
		stats = UnitStats()
		stats.Health.Value = 5
		stats.Damage.Value = 5
		self.__unit = GameUnit('unit', stats, UnitRace.Gnoll)
		
	def test_unit_init(self):
		# arrage
		race = UnitRace.Gnoll
		name = 'unit'
		stats = UnitStats()
		stats.Health.Value = 5
		stats.Damage.Value = 5
		# act
		unit = GameUnit(name, stats, race)
		# assert
		self.assertEqual(name, unit.Name)
		self.assertEqual(stats, unit.Stats)
		self.assertEqual(race, unit.Race)
	
	def test_unit_isalive(self):
		# act
		self.__unit.Stats.Health.Value = 1
		# assert
		self.assertTrue(self.__unit.IsAlive())
	
	def test_unit_isnotalive(self):
		# act
		self.__unit.Stats.Health.Improve(-5)
		# assert
		self.assertFalse(self.__unit.IsAlive())
	
	@patch('common.unitstrategy.UnitStrategy')
	def test_unit_action(self, MockStrategy):
		# arrage
		strategy = MockStrategy()
		self.__unit.SetStrategy(strategy)
		# act
		self.__unit.Action()
		# assert
		strategy.Action.assert_called_with(self.__unit.Uid)

if __name__== '__main__':
	unittest.main()