from menu import *
import commands


MainMenu = Menu()

def create_Menu():
    Menu1 = MenuItem(1, "New game", commands.new_game).item
    Menu2 = MenuItem(2, "Load game", "cmd").item
    Menu3 = MenuItem(3, "Exit", commands.exit).item

    MainMenu.add(Menu1)
    MainMenu.add(Menu2)
    MainMenu.add(Menu3)

    return MainMenu

MainMenu.printing_menu()


MainMenu.choose()
