from uuid import uuid4

class Uid():
	def __init__(self):
		self.__uid = uuid4()
	
	def __repr__(self):
		return str(self.__uid)
	
	def __str__(self):
		return str(self.__uid)