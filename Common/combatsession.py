from uid import Uid

class CombatSession():
	def __init__(self):
		self.__participants = {}
		self.__uid = Uid()
		
	@property
	def Uid(self) -> Uid:
		return self.__uid