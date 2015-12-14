from basic_elements import *
import commands_name_submenu

Name_SubMenu = Menu()


Menu1 = MenuItem(1, "Reenter name", commands_name_submenu.reenter_name).item
Menu2 = MenuItem(2, "Continue", commands_name_submenu.continuing).item
Menu3 = MenuItem(3, "Save", "save function").item
Menu4 = MenuItem(4, "Quit", commands_name_submenu.quitting).item


Name_SubMenu.add(Menu1)
Name_SubMenu.add(Menu2)
Name_SubMenu.add(Menu3)
Name_SubMenu.add(Menu4)
