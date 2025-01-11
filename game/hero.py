import random

class Hero:
    def __init__(self, name, strength, dexterity, vigor, intelligence, resistance):
        self.name = name
        self.level = 1
        self.exp = 0
        self.strength = strength
        self.dexterity = dexterity
        self.vigor = vigor
        self.intelligence = intelligence
        self.resistance = resistance
        self.max_floor = 0  # Piso máximo atingido

    def setFitness(self, fitness):
        self.fitness = fitness

    def getExp(self, exp):
        self.exp += exp
        if (self.exp >= 5 * self.level):
            self.__levelUp()

    def __levelUp(self):
        self.level += 1

    def __repr__(self):
        return (f"Hero {self.name}(strength={self.strength}, dexterity={self.dexterity}, "
                f"vigor={self.vigor}, intelligence={self.intelligence}, resistance={self.resistance})")
