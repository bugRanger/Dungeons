import unittest
from unittest.mock import MagicMock, patch
# import directories
import sys
sys.path.append('../units')
sys.path.append('../common')
sys.path.append('../common/enums')

from gnollnames import GnollNames

class GnollNameTest(unittest.TestCase):

	def test_name_without_tribal(self):
		# arrage
		diceMock = MagicMock(return_value=GnollNames.LOW_TRIBALNAME_ROLL - 1)
		gnollNameGen = GnollNames(diceMock)
		name = '{}{}'.format(GnollNames.FIRST_NAME[1], 
			GnollNames.SECONDS_NAME[1])
		# act
		nameGen = gnollNameGen.GetName()
		# assert
		self.assertEqual(nameGen, name)

	def test_name_with_tribal(self):
		# arrage
		diceMock = MagicMock(return_value=GnollNames.LOW_TRIBALNAME_ROLL + 1)
		gnollNameGen = GnollNames(diceMock)
		name = '{}{} {}{}'.format(GnollNames.FIRST_NAME[3], 
			GnollNames.SECONDS_NAME[3],
			GnollNames.THIRD_NAME[3],
			GnollNames.FOURTH_NAME[3])
		# act
		nameGen = gnollNameGen.GetName()
		# assert
		self.assertEqual(nameGen, name)

if __name__=='__main__':
	unittest.main()