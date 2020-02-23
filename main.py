# import directories
import sys
sys.path.append('./units')
sys.path.append('./common')
sys.path.append('./common/enums')

from uid import Uid
from strategyfactory import ConcreateMeleeStrategy
from unitfactory import UnitCreator, ConcreateGnoll
from namefactory import NameFactory, ConcreateGnollName
from combatsession import CombatSession

def MakeUnit(creator : UnitCreator, name : NameFactory):
	return creator.Make(name.Make())	
# TODO необходим прокси класс сервера.
# TODO через сессию боя передавать действия юнитов на сервер.
combat = CombatSession()

unit = MakeUnit(ConcreateGnoll(), ConcreateGnollName())
unit.SetStrategy(ConcreateMeleeStrategy().Make(combat))
combat.AppendUnit(unit)

unit2 = MakeUnit(ConcreateGnoll(), ConcreateGnollName())
unit2.SetStrategy(ConcreateMeleeStrategy().Make(combat))
#combat.AppendUnit(unit2)

print(unit)
unit.Action()

print('\n')

print(unit2)
unit2.Action() 