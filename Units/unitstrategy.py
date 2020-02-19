from abc import ABC, abstractmethod
from uid import Uid

class UnitStrategy(ABC):
	@abstractmethod
	def Action(self, unit : Uid):
		# TODO учесть состояние.
		pass