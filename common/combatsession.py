from typing import Dict

from common.uid import Uid
from common.gameunit import GameUnit

'''
	Отслеживание состояния боя, завершение.
'''
# TODO Определиться с назначением.
class CombatSession():
	__participants : Dict[Uid, GameUnit] = {}
	
	# TODO Поток для действий участников.
	# __actions = ThreadQueue()
		
	
	# TODO попахиаает высокой связанностью.
	def GetParticipants(self, expression):
		return list(filter(expression, self.__participants.values()))
	
	def HandleParticipantUpdate(self):
		pass

	def ContainsUnit(self, uid: Uid):
		return uid in self.__participants
		
	def AppendUnit(self, unit: GameUnit):
		self.__participants[unit.Uid] = unit
		
	def RemoveUnit(self, uid: Uid):
		self.__participants.pop(uid, None)