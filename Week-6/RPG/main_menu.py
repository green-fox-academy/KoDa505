from basic_elements import *
import commands

MainMenu = Menu()


Menu1 = MenuItem(1, "New game", commands.new_game)
Menu2 = MenuItem(2, "Load game", "cmd")
Menu3 = MenuItem(3, "Exit", commands.exiting)


MainMenu.add(Menu1)
MainMenu.add(Menu2)
MainMenu.add(Menu3)


MainMenu.printing_menu()
MainMenu.choose()
