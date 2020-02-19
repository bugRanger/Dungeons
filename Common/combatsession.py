from uid import Uid
from gameunit import GameUnit

class CombatSession():
	def __init__(self):
		self.__participants = {}
		self.__uid = Uid()
		
	@property
	def Uid(self) -> Uid:
		return self.__uid

	def ContainsUnit(self, uid: Uid):
		return uid in self.__participants
		
	def AppendUnit(self, unit: GameUnit):
		self.__participants[unit.Uid] = unit
		
	def RemoveUnit(self, uid: Uid):
		self.__participants.pop(uid, None)