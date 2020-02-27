from common.namegenerator import NameGenerator

class GnollNames(NameGenerator):
    # Syllables
    FIRST_NAME = ["Ga" , "Der" , "Gre" , "Rem" , "Thu"]
    SECONDS_NAME = ["mock" , "ror" , "rr" , "mar" , "rrg"]
    # Tribalname 
    THIRD_NAME = ["True" , "Blood" , "Great" , "Spear" , "Thunder"]
    FOURTH_NAME = ["feather", "fist", "fang", "death", "dance"]
    # Tribalname dice roll
    TRIBALNAME_COUNT_DICE = 2
    TRIBALNAME_FACETS_DICE = 12
    LOW_TRIBALNAME_ROLL = 2
    HIGH_TRIBALNAME_ROLL = 8

    def __init__(self, diceDrop):
        self.__diceDrop = diceDrop
	
    def HasTribalname(self):
        rng = range(0, self.TRIBALNAME_FACETS_DICE)
        drop = self.__diceDrop(self.TRIBALNAME_COUNT_DICE, rng)
        return self.LOW_TRIBALNAME_ROLL < drop < self.HIGH_TRIBALNAME_ROLL

    def GetName(self) -> str:
        def DropForNames(names):
            dropIndex = self.__diceDrop(1, range(0, len(names)))
            return names[dropIndex]
        
        name = ''
        s1 = DropForNames(self.FIRST_NAME)
        s2 = DropForNames(self.SECONDS_NAME)

        if self.HasTribalname():
            t1 = DropForNames(self.THIRD_NAME)
            t2 = DropForNames(self.FOURTH_NAME)
            name += '{}{} {}{}'.format(s1, s2, t1, t2)
        else:
            name = '{}{}'.format(s1, s2)

        return name