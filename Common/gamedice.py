from random import randint

class GameDice:
	@staticmethod
	def Drop(count : int, facets):
		result = 0
		if count != 0 and len(facets) != 0:
			for i in range(0, count):
				result += facets[randint(0, len(facets) - 1)]
		return result