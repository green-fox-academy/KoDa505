import random

class Player:
    def __init__(self, name = "Anonim", dexterity = 0, health = 0, luck = 0):
        self.name = name
        self.dexterity = dexterity
        self.health = health
        self.luck = luck

    def display(self):
        return {"name": self.name, "health":self.health, "dexterity": self.dexterity, "luck":self.luck}

    def display_print(self):
        print("{} D: {} H: {} L: {}".format(self.name, self.dexterity, self.health, self.luck))

    def shuffle_properties(self):
        d = random.randint(1,6)
        self.dexterity = d + 6
        print("Your dexterity is: " + str(self.dexterity))
        d1 = random.randint(1,6)
        d2 = random.randint(1,6)
        self.health = d1 + d2 + 12
        print("Your health is: " + str(self.health))
        d = random.randint(1,6)
        self.luck = d + 6
        print("Your luck is: " + str(self.luck))


player1 = Player()
