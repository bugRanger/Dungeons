from enum import Enum

class UnitRace(Enum):
	Gnoll = 0
	Human = 1
	Goblin = 2
	Elf = 3
	Orc = 4

	def __str__(cls):
		return cls.name