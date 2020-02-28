import unittest
 
from common.gamedice import GameDice

class GameDiceTest(unittest.TestCase):
	
	def test_dice_drop_0(self):
		# act
		dropEmptyList = GameDice.Drop(1, [])
		dropZeroCount = GameDice.Drop(0, [5])
		# assert
		self.assertEqual(dropEmptyList, 0)
		self.assertEqual(dropZeroCount, 0)
		
	def test_dice_drop_5(self):
		# act
		drop = GameDice.Drop(1, [5])
		# assert
		self.assertEqual(drop, 5)
	
	def test_dice_drop_10(self):
		# act
		drop = GameDice.Drop(2, [5])
		# assert
		self.assertEqual(drop, 10)
		
	def test_dice_drop_5or6(self):
		# act
		drop = GameDice.Drop(1, [5, 6])
		# assert
		self.assertTrue(drop == 5 or drop == 6)
		
	def test_dice_drop_between10and12(self):
		# act
		drop = GameDice.Drop(2, [5, 6])
		# assert
		self.assertLessEqual(drop, 12)
		self.assertGreaterEqual(drop, 10)
	
	def test_dice_drop_for_perc20(self):
		# arrage
		perc = 0
		facets = [1, 1, 1, 1, 3]
		# act
		for i in range(0, 10000):
			drop = GameDice.Drop(1, facets)
			if drop == 3:
				perc += 1
		perc = perc/10000*100
		# assert
		self.assertLessEqual(perc, 21)
		self.assertGreaterEqual(perc, 19)
	
if __name__ == '__main__':
	unittest.main()