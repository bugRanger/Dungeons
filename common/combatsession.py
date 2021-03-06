from common.uid import Uid
from common.gameunit import GameUnit

class CombatSession():
	def __init__(self):
		self.__participants = {}
		# TODO Поток для действий участников.
		# self.__actions = ThreadQueue()

	def GetParticipants(self, expression):
		return list(filter(expression, self.__participants.values()))
		
	def ContainsUnit(self, uid: Uid):
		return uid in self.__participants
		
	def AppendUnit(self, unit: GameUnit):
		self.__participants[unit.Uid] = unit
		
	def RemoveUnit(self, uid: Uid):
		self.__participants.pop(uid, None)
