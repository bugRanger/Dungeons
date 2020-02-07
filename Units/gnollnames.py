from random import randint, random
from namegenerator import NameGenerator

class GnollNames(NameGenerator):
    def __init__(self):
        # Syllables
        self.__first = [ "Ga" , "Der" , "Gre" , "Rem" , "Thu" ]
        self.__second = [ "mock" , "ror" , "rr" , "mar" , "rrg" ]
        # Tribalname 
        self.__third = [ "True" , "Blood" , "Great" , "Spear" , "Thunder" ]
        self.__fourth = [ "feather", "fist", "fang", "death", "dance" ]
    
    def GetRandom(self) -> str:
        s1 = randint(0, len(self.__first) - 1)
        s2 = randint(0, len(self.__second) - 1)

        name = "{0}{1}".format(self.__first[s1], self.__second[s2])

        if 2 < randint(0, 10) < 8:
            t1 = randint(0, len(self.__third) - 1)
            t2 = randint(0, len(self.__fourth) - 1)
            name += " " + self.__third[t1] + self.__fourth[t2]

        return name