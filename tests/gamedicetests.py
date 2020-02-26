import unittest

# import directories
import sys
sys.path.append('../units')
sys.path.append('../common')
sys.path.append('../common/enums')

from gamedice import GameDice

class GameDiceTest(unittest.TestCase):
	
	def test_drop_0(self):
		# act
		dropEmptyList = GameDice.Drop(1, [])
		dropZeroCount = GameDice.Drop(0, [5])
		# assert
		self.assertEqual(dropEmptyList, 0)
		self.assertEqual(dropZeroCount, 0)
		
	def test_drop_5(self):
		# act
		drop = GameDice.Drop(1, [5])
		# assert
		self.assertEqual(drop, 5)
	
	def test_drop_10(self):
		# act
		drop = GameDice.Drop(2, [5])
		# assert
		self.assertEqual(drop, 10)
		
	def test_drop_5or6(self):
		# act
		drop = GameDice.Drop(1, [5, 6])
		# assert
		self.assertTrue(drop == 5 or drop == 6)
		
	def test_drop_between10and12(self):
		# act
		drop = GameDice.Drop(2, [5, 6])
		# assert
		self.assertTrue(10 <= drop <= 12)
		
if __name__ == '__main__':
	unittest.main()