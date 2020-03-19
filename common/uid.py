from uuid import uuid4

# TODO Add group unit.
class Uid():
	# const
	EMPTY_GROUP = 0
	DEFAULT_PATTERN = '{}@group:{}'
	
	def __init__(self, group : int = EMPTY_GROUP):
		self.__uid = uuid4()
		self.__group = group
	
	# TODO попахивает.
	@property
	def Group(self)->int:
		return self.__group
	
	def __repr__(self):
		return self.__str__()
	
	def __str__(self):
		return self.DEFAULT_PATTERN.format(str(self.__uid), 
			self.__group)