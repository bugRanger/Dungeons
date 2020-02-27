from abc import ABC, abstractmethod

from common.uid import Uid

class UnitStrategy(ABC):
	@abstractmethod
	def Action(self, unit : Uid):
		# TODO учесть состояние.
		pass