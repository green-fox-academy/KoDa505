from basic_elements import *
import commands_reroll_submenu


Reroll_SubMenu = Menu()


Menu1 = MenuItem(1, "Reroll stats", commands_reroll_submenu.reroll)
Menu2 = MenuItem(2, "Continue", commands_reroll_submenu.potion_choosing)
Menu3 = MenuItem(3, "Save", "save function")
Menu4 = MenuItem(4, "Quit", commands_reroll_submenu.quitting)


Reroll_SubMenu.add(Menu1)
Reroll_SubMenu.add(Menu2)
Reroll_SubMenu.add(Menu3)
Reroll_SubMenu.add(Menu4)
