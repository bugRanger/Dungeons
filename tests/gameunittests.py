import unittest
from unittest.mock import patch

# import directories
import sys
sys.path.append('../units')
sys.path.append('../common')
sys.path.append('../common/enums')

from gameunit import GameUnit, UnitRace

class GameUnitTests(unittest.TestCase):
	def setUp(self):
		self.__unit = GameUnit('unit', 'desc', 1, 1, UnitRace.Gnoll)
		
	def test_init(self):
		# arrage
		name = 'unit'
		desc = 'desc'
		health = 1
		damage = 1
		race = UnitRace.Gnoll
		
		# act
		unit = GameUnit(name, desc, health, damage, race)
		
		# assert
		self.assertEqual(name, unit.Name)
		self.assertEqual(desc, unit.Desc)
		self.assertEqual(health, unit.Health)
		self.assertEqual(damage, unit.Damage)
		self.assertEqual(race, unit.Race)
	
	def test_isalive(self):
		 #act
		self.__unit.Health = 1;
		
		#assert
		self.assertTrue(self.__unit.IsAlive())
	
	def test_isnotalive(self):
		 #act
		self.__unit.Health -= self.__unit.Health;
		
		#assert
		self.assertFalse(self.__unit.IsAlive())
	
	@patch('unitstrategy.UnitStrategy')
	def test_action(self, MockStrategy):
		# arrage
		strategy = MockStrategy()
		self.__unit.SetStrategy(strategy)
		
		# act
		self.__unit.Action()
		
		# assert.
		strategy.Action.assert_called_with(self.__unit.Uid)

if __name__== '__main__':
	unittest.main()