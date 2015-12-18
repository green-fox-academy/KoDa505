import random

class Monster:
    def __init__(self, name, dexterity, health):
        self.name = name
        self.dexterity = dexterity
        self.health = health

    def display(self):
        return {
            "name": self.name, "health":self.health, "dexterity": self.dexterity
        }

    def display_print(self):
        print("\n{} \nD: {} H: {} L: {} \nInventory: \n   Sword: {}\n   Leather armor: {}\n   Potion: {} ".format(self.name, self.dexterity, self.health, self.luck, self.sword, self.leather_armor, self.potion))

    def shuffle_properties(self):
        d = random.randint(1,15)
        self.dexterity = d
        d1 = random.randint(1,30)
        self.health = d1

    def fight_print(self):
        print("\nYour enemy's name: {} \n   Its dexterity: {}\n   Its  health: {}".format(self.name, self.dexterity, self.health))

    def strike(self):
        d1 = random.randint(1,6)
        d2 = random.randint(1,6)
        fight_point = d1 + d2 + self.dexterity
        return fight_point



monster = Monster("John", 1, 1)
monster.shuffle_properties()
