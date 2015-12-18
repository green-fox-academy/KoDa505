from menu_class import *
import player
import monster

BeginMenu = Menu()


Menu1 = MenuItem(1, "Begin", 'begin')
Menu2 = MenuItem(2, "Save", "exiting")
Menu3 = MenuItem(3, "Quit", "save function")


BeginMenu.add(Menu1)
BeginMenu.add(Menu2)
BeginMenu.add(Menu3)

def strikemenu():
    StrikeMenu = Menu()
    Menu1 = MenuItem(1, "Strike", strike)
    Menu2 = MenuItem(2, "Retreat", 'retreart')
    Menu3 = MenuItem(3, "Quit", 'quit')
    StrikeMenu.add(Menu1)
    StrikeMenu.add(Menu2)
    StrikeMenu.add(Menu3)
    StrikeMenu.printing_menu()
    StrikeMenu.choose()

def begin():
    print("****" *10 + "\n"+ "Test your Sword in a test fight")
    player.player1.fight_print()
    monster.monster.fight_print()
    strikemenu()

def strike():
    print("Your hit was" + str(player.player1.strike()) + "its hit was" + str(monster.monster.strike()))
    if player.player1.strike() >  monster.monster.strike():
        return "You won"
    if player.player1.strike() <  monster.monster.strike():
        return "It won"
