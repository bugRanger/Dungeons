import unittest
from unittest.mock import patch

from common.gameunit import GameUnit, UnitRace
from common.unitstats import UnitStats

class GameUnitTests(unittest.TestCase):
	def setUp(self):
		stats = UnitStats()
		stats.Health = 1
		stats.Damage = 1
		self.__unit = GameUnit('unit', 'desc', stats, 
			UnitRace.Gnoll)
		
	def test_unit_init(self):
		# arrage
		race = UnitRace.Gnoll
		name = 'unit'
		desc = 'desc'
		stats = UnitStats()
		stats.Health = 1
		stats.Damage = 1
		# act
		unit = GameUnit(name, desc, stats, race)
		# assert
		self.assertEqual(name, unit.Name)
		self.assertEqual(desc, unit.Desc)
		self.assertEqual(stats.Health, unit.Health)
		self.assertEqual(stats.Damage, unit.Damage)
		self.assertEqual(race, unit.Race)
	
	def test_unit_isalive(self):
		#act
		self.__unit.Health = 1
		
		#assert
		self.assertTrue(self.__unit.IsAlive())
	
	def test_unit_isnotalive(self):
		#act
		self.__unit.Health -= self.__unit.Health
		
		#assert
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