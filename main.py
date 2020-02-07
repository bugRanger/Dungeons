import sys
# import work directories
sys.path.append('./units')
sys.path.append('./common')
sys.path.append('./common/enums')

from unitfactory import UnitCreator, ConcreateGoblin
	
def MakeUnit(creator : UnitCreator, name=''):
	return creator.Make(name)

print(MakeUnit(ConcreateGoblin()))