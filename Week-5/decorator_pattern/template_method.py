import random

class Warrior:
    def __init__(self, weapon):
        self.hp = 100
        self.weapon = weapon

    def strike(self, other):
        self.weapon.strike(self, other)

    def __repr__(self):
        return "Warrior hp: {}".format(self.hp)


class Weapon:
    def __init__(self):
        pass

    def damage(self):
        raise "not implemented"

    def self_damage():
        raise "not implemented"

    def strike(self, warrior, other):
        other.hp -= self.damage()
        warrior.hp -= self.self_damage()

class Sword(Weapon):

    def damage(self):
        return 10

    def self_damage(self):
        return 0

class Mace(Weapon):
    def damage(self):
        return 50

    def self_damage(self):
        return 20

class CriticalSword(Weapon):
    def damage(self):
        return 10 + random.randint(0,10)

    def self_damage(self):
        return 2

class Enchanted(Weapon):
    def __init__(self, weapon):
        self.weapon = weapon


    def damage(self):
        return self.weapon.damage() * 2

    def self_damage(self):
        return self.weapon.self_damage() / 2


warrior = Warrior(Sword())
monster = Warrior(Mace())

warrior.strike(monster)
print(warrior)
print(monster)

warrior = Warrior(Enchanted(Sword()))
warrior.strike(monster)

print(warrior)
print(monster)
