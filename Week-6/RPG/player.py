import random

class Player:
    def __init__(self, name = "Anonim", dexterity = 0, max_health = 0, health = 0, max_luck = 0, luck = 0, potion = None, sword = 1, leather_armor = 1):
        self.name = name
        self.dexterity = dexterity
        self.max_health = max_health
        self.health = health
        self.max_luck = max_luck
        self.luck = luck
        self.potion = potion
        self.leather_armor = leather_armor
        self.sword = sword

    def display(self):
        return {
            "name": self.name, "health":self.health, "dexterity": self.dexterity, "luck":self.luck, "potion": self.potion,
            "sword": self.sword, "leather_armor": self.leather_armor
        }

    def display_print(self):
        print("\n{} \nD: {} H: {} L: {} \nInventory: \n   Sword: {}\n   Leather armor: {}\n   Potion: {} ".format(self.name, self.dexterity, self.health, self.luck, self.sword, self.leather_armor, self.potion))

    def shuffle_properties(self):
        d = random.randint(1,6)
        self.dexterity = d + 6
        print("Your dexterity is: " + str(self.dexterity))
        d1 = random.randint(1,6)
        d2 = random.randint(1,6)
        self.health = d1 + d2 + 12
        self.max_health = d1 + d2 + 12
        print("Your health is: " + str(self.health))
        d = random.randint(1,6)
        self.luck = d + 6
        self.max_luck = d + 6
        print("Your luck is: " + str(self.luck))


    def potion_dexterity(self):
        self.potion = "Dexterity"

    def potion_health(self):
        self.potion = "Health"

    def potion_luck(self):
        self.potion = "Luck"

    def fight_print(self):
        print("\nYour name: {} \n   Your dexterity: {}\n   Your current luck: {}\n   Your max luck: {}\n   Your current health: {}\n   Your max health: {}".format(self.name, self.dexterity, self.luck, self.max_luck, self.health, self.max_health))

    def strike(self):
        d1 = random.randint(1,6)
        d2 = random.randint(1,6)
        fight_point = d1 + d2 + self.dexterity
        return fight_point        


player1 = Player()
