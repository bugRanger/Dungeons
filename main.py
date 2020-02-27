from common.uid import Uid
from common.combatsession import CombatSession
from unit.strategyfactory import ConcreateMeleeStrategy
from unit.unitfactory import UnitCreator, ConcreateGnoll
from unit.namefactory import NameFactory, ConcreateGnollName

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