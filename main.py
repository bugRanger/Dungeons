import sys
# import work directories
sys.path.append('./units')
sys.path.append('./common')
sys.path.append('./common/enums')

from unitfactory import UnitCreator, ConcreateGnoll
from namefactory import NameFactory, ConcreateGnollName

def MakeUnit(creator : UnitCreator, name : NameFactory):
	return creator.MakeUnit(name.MakeName())

unit = MakeUnit(ConcreateGnoll(), ConcreateGnollName())
print(unit.Name)