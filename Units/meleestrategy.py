from uid import Uid
from unitstrategy import UnitStrategy
from combatsession import CombatSession

class MeleeStrategy(UnitStrategy):
	def __init__(self, session: CombatSession):
		self.__session = session
		self.__target = None
		
	def Action(self,  unit: Uid):
		targets = self.__session.GetParticipants(lambda x: x.Uid != unit)
		self.__target = targets[0] if any(targets) else None
		
		# TODO harm, help типы целей и заклятий
		# TODO Получить от сесии цель, применить к ней действие.
		print('Target: {}'.format(self.__target.Uid if self.__target != None else None))
