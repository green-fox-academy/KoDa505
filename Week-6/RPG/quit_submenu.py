from menu_class import *
import commands_name_submenu

Quit_SubMenu = Menu()

def exiting():
    exit()

Menu1 = MenuItem(1, "Save and Quit", "sfhoi")
Menu2 = MenuItem(2, "Quit without save", exiting)
Menu3 = MenuItem(3, "Resume", "save function")


Quit_SubMenu.add(Menu1)
Quit_SubMenu.add(Menu2)
Quit_SubMenu.add(Menu3)
