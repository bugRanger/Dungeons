'''
	Negative and positive unit stats/buffs/items.
	Current unit stats cannot be negative after update.
'''
class BasicStat():
	# Constructor
	def __init__(self, value):
		self.__value = value
	
	# Properties
	@property
	def Value(self):
		return self.GetValue()
		
	# Methods
	def GetValue(self):
		return self.__value
		
	# Override
	def __str__(self):
		return str(self.Value)

class UnitStat(BasicStat):
	# Constructor
	def __init__(self, value):
		super().__init__(value)
		self.__modified = 0
		self.__min = 0
		self.__max = None

	# Properties
	@property
	def Modified(self):
		return self.__modified
		
	@property
	def Min(self):
		return self.__min
		
	@Min.setter
	def Min(self, value):
		self.__min = value
		
	@property
	def Max(self):
		return self.__max
		
	@Max.setter
	def Max(self, value):
		self.__max = value

	# Methods
	def Improve(self, value):
		self.__modified = self.ImproveImp(value)

	def CalcImp(self, modified):
		return super().GetValue() + modified

	def ImproveImp(self, modified):
		return self.__modified + modified
	
	# Override
	def GetValue(self):
		value = self.CalcImp(self.__modified)
		if self.__max != None and value > self.__max:
			return self.__max
		elif value < self.__min:
			return self.__min
		else:
			return value
'''
	Unit stats.
'''
class Health(UnitStat):
	# Constructor
	def __init__(self, value):
		super().__init__(value) 
		self.Max = value

class Damage(UnitStat):
	# Constructor
	def __init__(self, value):
		super().__init__(value) 
		self.Min = 1
	
class CritRate(UnitStat):
	# Constructor
	def __init__(self, value):
		super().__init__(value) 
		self.Max = 100
'''
	Container for unit stats.
'''
class UnitStats:
	# Constructor
	def __init__(self):
		# TODO Add stats:
		# % crit, hit, dodge and others
		self.__health = Health(1)
		self.__damage = Damage(1)
		self.__critRate = CritRate(5)
		
	# Properties
	def Health(self) -> Health:
		return self.__health
		
	def Damage(self) -> Damage:
		return self.__damage
		
	def CritRate(self) -> CritRate:
		return self.__critRate
