from basic_elements import *
import commands_reroll_submenu

Reroll_SubMenu = Menu()


Menu1 = MenuItem(1, "Reroll stats", commands_reroll_submenu.reroll).item
Menu2 = MenuItem(2, "Continue", "kuigig").item
Menu3 = MenuItem(3, "Save", "save function").item
Menu4 = MenuItem(4, "Quit", "save function").item


Reroll_SubMenu.add(Menu1)
Reroll_SubMenu.add(Menu2)
Reroll_SubMenu.add(Menu3)
Reroll_SubMenu.add(Menu4)
