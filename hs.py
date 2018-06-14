import sys
import os
import math

class card():
    type = None
    name = None
    cost = None

    def __init__(self, name, type, cost):
        self.name = name
        self.type = type
        self.cost = cost

    def getName(self):
        return self.name

    def getType(self):
        return self.type

    def getCost(self):
        return self.cost

    def printInfo(self):
        infoStr = ("Card Name: " + self.name + " Card Type: " + self.type + " Cost: " + str(self.cost))
        return infoStr

class minion(card):
    attack = -1
    health = -1

    def __init__(self, name, type, cost, attack, health):
        self.attack = attack
        self.health = health
        super(minion, self).__init__(name, type, cost)

    def getAttack(self):
        return self.attack

    def getHealth(self):
        return self.health

    def printInfo(self):
        infoStr = (super(minion, self).printInfo() + " Minion Attack: " + str(self.attack) + " Minion Health: " + str(self.health))
        return infoStr

class effectMinion(minion):
    effect = None

    def __init__(self, name, type, cost, attack, health, effect):
        self.effect = effect
        super(minion, self).__init__(name, type, cost, attack, health)

    def getEffect(self):
        return self.effect

    def printInfo(self):
        infoStr = (super(effectMinion, self).printInfo())

class spell(card):
    isSpell = None

    def __init__(self, name, type, cost, isp):
        self.isSpell = isp
        super(spell, self).__init__(name, type, cost)

    def isSpell(self):
        return self.isSpell

    def printInfo(self):
        infoStr = (super(spell, self).printInfo() + " Is Spell: " + str(self.isSpell))
        return infoStr

print("HS Card")
dkgar = card("Scourgelord Garrosh", "Hero Card", 8)
tinkmaster = minion("Tinkmaster Overspark", "Minion", 3, 3, 3)
uportal = spell("Unstable Portal", "Spell", 2, True)

print(dkgar.printInfo())
print(tinkmaster.printInfo())
print(uportal.printInfo())