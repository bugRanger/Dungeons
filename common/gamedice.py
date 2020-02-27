from random import randint

class GameDice:
	'''
	A generator to get a random number.
	count - the number of throws.
	facets - can be like unique queue or not.
	'''
	@staticmethod
	def Drop(count : int, facets):
		result = 0
		if count != 0 and len(facets) != 0:
			for i in range(0, count):
				result += facets[randint(0, len(facets) - 1)]
		return result