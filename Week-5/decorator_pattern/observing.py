class Warrior:
    def __init__(self):
        self.companions = []
        self.hp = 100
        self.carrot = 500

    def join(self, companion):
        self.companions.append(companion)

    def strike(self, opponent):
        opponent.inflict_damage(10)

    def curse(self, opponent):
        opponent.join(Curse())
        pass

    def inflict_damage(self, damage):
        self.hp -= damage
        for companion in self.companions:
            companion.notify("damage", self)

    def giving_carrot(self, carrot):
        self.carrot += carrot
        for companion in self.companions:
            companion.notify('carrot', self)

    def heal(self, hp):
        self.hp += hp


class Healer:
    def __init__(self):
        self.carrot = 400

    def notify(self, type, warrior):
        if type == "damage":
            warrior.heal(10)
        if type == 'carrot':
            self.carrot += 5
            warrior.carrot -= 5

class Curse:
    def notify(self, type, warrior):
        if type == 'damage':
            warrior.heal(-10)


rabbit = Warrior()
wolf = Warrior()
shaman = Healer()

rabbit.join(shaman)

print(rabbit.hp)
wolf.strike(rabbit)
print(rabbit.hp)
wolf.curse(rabbit)
print(rabbit.hp)

print("Shaman's carrots:", shaman.carrot)
print("rabbit's carrots:", rabbit.carrot)

rabbit.giving_carrot(30)

print(shaman.carrot)
print(rabbit.carrot)
