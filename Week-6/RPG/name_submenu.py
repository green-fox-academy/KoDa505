from menu_class import *
import commands_name_submenu

Name_SubMenu = Menu()


Menu1 = MenuItem(1, "Reenter name", commands_name_submenu.reenter_name)
Menu2 = MenuItem(2, "Continue", commands_name_submenu.continuing)
Menu3 = MenuItem(3, "Save", commands_name_submenu.save)
Menu4 = MenuItem(4, "Quit", commands_name_submenu.quitting)


Name_SubMenu.add(Menu1)
Name_SubMenu.add(Menu2)
Name_SubMenu.add(Menu3)
Name_SubMenu.add(Menu4)
