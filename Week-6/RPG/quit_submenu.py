from basic_elements import *
import commands_quit_submenu

Quit_SubMenu = Menu()


Menu1 = MenuItem(1, "Save and Quit", "com").item
Menu2 = MenuItem(2, "Quit without save", "Continue").item
Menu3 = MenuItem(3, "Resume", "save function").item


Quit_SubMenu.add(Menu1)
Quit_SubMenu.add(Menu2)
Quit_SubMenu.add(Menu3)
