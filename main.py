import sys
# import work directories
sys.path.append('./units')
sys.path.append('./common')
sys.path.append('./common/enums')

from uid import Uid
from unitstrategy import MeleeStrategy
from unitfactory import UnitCreator, ConcreateGnoll
from namefactory import NameFactory, ConcreateGnollName
from combatsession import CombatSession

def MakeUnit(creator : UnitCreator, name : NameFactory):
	return creator.MakeUnit(name.MakeName())

# TODO add unit strategy, actions() -> defenve | attack | other
unit = MakeUnit(ConcreateGnoll(), ConcreateGnollName())
unit.SetStrategy(MeleeStrategy())

print(unit)