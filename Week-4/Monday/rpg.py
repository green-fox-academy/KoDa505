class GameCharacter:
    def __init__(self, name, HP, damage):
        self.name = name
        self.HP = HP
        self.damage = damage

    def print_status(self):
        if self.HP == 0:
            print(self.name + "Dead")
        else:
            print('Its name is {} and its health points are {}'.format(self.name, self.HP))


    def drink_potion(self):
        self.HP += 10

    def strike(self, enemy):
        enemy.HP -= self.damage
        print('Enemy HP: ' + str(enemy.HP))



class Cleric(GameCharacter):
    def heal(self, ally):
        ally.HP += 10


balrog = GameCharacter('Balrog', 100, 20)
wizard = GameCharacter('Wizard', 50, 40)
melkor = Cleric('Melkor', 1000, 80)

balrog.print_status()
for i in range(3):
    wizard.strike(balrog)
    melkor.heal(balrog)
balrog.drink_potion()
