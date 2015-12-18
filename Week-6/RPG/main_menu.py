from menu_class import *
import commands

MainMenu = Menu()


Menu1 = MenuItem(1, "New game", commands.MainMenu.new_game)
Menu2 = MenuItem(2, "Load game", "cmd")
Menu3 = MenuItem(3, "Exit", commands.MainMenu.exiting)


MainMenu.add(Menu1)
MainMenu.add(Menu2)
MainMenu.add(Menu3)
