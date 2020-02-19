from uid import Uid
from unitstrategy import UnitStrategy
from combatsession import CombatSession

class MeleeStrategy(UnitStrategy):
	def __init__(self, session: CombatSession):
		self.__session = session
		
	def Action(self,  unit: Uid):
		print("Attack")