from common.uid import Uid
from common.combatsession import CombatSession
from common.unitstrategy import UnitStrategy

class MeleeStrategy(UnitStrategy):
	def __init__(self, session: CombatSession):
		self.__session = session
		self.__target = None
		
	def Action(self,  unit: Uid):
		filter = lambda x: x.Uid != unit
		targets = self.__session.GetParticipants(filter)
		self.__target = targets[0] if any(targets) else None
		
		# TODO harm, help типы целей и заклятий
		# TODO Получить от сесии цель, применить к ней действие.
		print('Target: {}'.format(self.__target.Uid if self.__target != None else None))
