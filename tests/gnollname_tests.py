import unittest
from unittest.mock import MagicMock

from unit.gnollnames import GnollNames

class GnollNameTest(unittest.TestCase):

	def test_generation_name_without_tribal(self):
		# arrage
		i = GnollNames.LOW_TRIBALNAME_ROLL - 1
		diceMock = MagicMock(return_value=i)
		gnollNameGen = GnollNames(diceMock)
		name = '{}{}'.format(GnollNames.FIRST_NAME[i], 
			GnollNames.SECONDS_NAME[i])
		# act
		nameGen = gnollNameGen.GetName()
		# assert
		self.assertEqual(nameGen, name)

	def test_generation_name_with_tribal(self):
		# arrage
		i = GnollNames.LOW_TRIBALNAME_ROLL + 1
		diceMock = MagicMock(return_value=i)
		gnollNameGen = GnollNames(diceMock)
		name = '{}{} {}{}'.format(GnollNames.FIRST_NAME[i], 
			GnollNames.SECONDS_NAME[i],
			GnollNames.THIRD_NAME[i],
			GnollNames.FOURTH_NAME[i])
		# act
		nameGen = gnollNameGen.GetName()
		# assert
		self.assertEqual(nameGen, name)

if __name__=='__main__':
	unittest.main()
