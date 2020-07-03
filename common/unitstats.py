'''
	Negative and positive unit stats/buffs/items.
	Current unit stats cannot be negative after update.
'''
import math

class Setter():
	def __init__(self, func, doc = None):
		self.__func = func
		self.__doc__ = doc if doc is not None else func.__doc__
		
	def __set__(self, obj, value):
		self.__func(obj, value)

class BasicStat():
	# Constructor
	def __init__(self, value):
		self.__value = value
		self.__onUpdated = None
	
	# Properties
	@property
	def Value(self):
		return self.GetValue()
	
	@Value.setter
	def Value(self, value):
		self.SetValue(value)

	@Setter
	def Updated(self, value):
		self.__onUpdated = value

	# Methods
	def GetValue(self):
		return self.__value
	
	def SetValue(self, value):
		self.__value = value
		if self.__onUpdated != None:
			self.__onUpdated(value)

	# Override
	def __str__(self):
		return str(self.Value)

class UnitStat(BasicStat):
	# Constructor
	def __init__(self, value):
		super().__init__(value)
		self.__onImproved = None
		# modified of value
		self.__modified = 0
		# mask of value
		self.__min = 0
		self.__max = None
	
	def __iadd__(self, stat: BasicStat):
		self._BasicStat__value += stat._BasicStat__value
		return self

	def __isub__(self, stat: BasicStat):
		self._BasicStat__value -= stat._BasicStat__value
		return self

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

	@Setter
	def Improved(self, value):
		self.__onImproved = value

	# Methods
	def Improve(self, value):
		self.__modified = self.ImproveImp(value)
		if self.__onImproved != None:
			self.__onImproved(value)

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

	def SetValue(self, value):
		super().SetValue(value)
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

class Experience(UnitStat):
	# Constructor
	def __init__(self, value):
		super().__init__(value)
	
	def SetValue(self, value):
		super().SetValue(value)
	
class Level(UnitStat):
	# Constructor
	def __init__(self, value):
		super().__init__(value)
		self.Min = 1
		self.Max = 5
		
	# Methods
	def SetValue(self, value):
		super().SetValue(value)
		self.Max = value

'''
	Container for unit stats.
'''
class UnitStats:
	# Constructor
	def __init__(self):
		# TODO Add stats:
		# % crit, hit, dodge and others
		self.__level = Level(0)
		self.__level.Updated  = self.__onLvlUpdated__
		self.__experience = Experience(0)
		self.__experience.Improved = self.__onExpImproved__
		self.__health = Health(1)
		self.__damage = Damage(1)
		self.__critRate = CritRate(5)
		self.__level.Value = 1
		
	# Properties
	@property
	def Level(self) -> Level:
		return self.__level
		
	@property
	def Experience(self) -> Experience:
		return self.__experience
	
	@property
	def Health(self) -> Health:
		return self.__health
		
	@property
	def Damage(self) -> Damage:
		return self.__damage
		
	@property
	def CritRate(self) -> CritRate:
		return self.__critRate
	
	def __onLvlUpdated__(self, value):
		self.UpdateLevel(value)
		
	def UpdateLevel(self, value):
		self.__experience.Max = value * 3 + value
	
	def __onExpImproved__(self, value):
		if self.__experience.Value >= self.__experience.Max : 
			self.__level.Value += math.trunc(value/3)

	def __str__(self):
		return 'Level: {}\nExp: {}/{}\nHealth: {}\nDamage: {}\nCrit: {}%'.format(self.__level, self.__experience, self.__experience.Max, self.__health, self.__damage, self.__critRate)
