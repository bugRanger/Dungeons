class GameObject:
	def __init__(self, name : str ='', desc : str =''):
		self.__name = name
		self.__desc = desc
		
	@property
	def Name(self):
		return self.__name
		
	@property
	def Desc(self):
		return self.__desc