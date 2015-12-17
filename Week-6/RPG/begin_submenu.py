from basic_elements import *
import player
import monster

BeginMenu = Menu()

def begin():
    print("Test your Sword in a test fight")
    player.player1.fight_print()
    monster.monster.fight_print()


Menu1 = MenuItem(1, "Begin", begin)
Menu2 = MenuItem(2, "Save", "exiting")
Menu3 = MenuItem(3, "Quit", "save function")


BeginMenu.add(Menu1)
BeginMenu.add(Menu2)
BeginMenu.add(Menu3)
