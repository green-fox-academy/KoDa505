from basic_elements import *
import commands_quit_submenu

Name_SubMenu = Menu()


Menu1 = MenuItem(1, "Reenter name", commands_quit_submenu.reenter_name).item
Menu2 = MenuItem(2, "Continue", "Continue function").item
Menu3 = MenuItem(3, "Save", "save function").item
Menu4 = MenuItem(4, "Quit", commands_quit_submenu.quitting).item


Name_SubMenu.add(Menu1)
Name_SubMenu.add(Menu2)
Name_SubMenu.add(Menu3)
Name_SubMenu.add(Menu4)


#Name_SubMenu.printing_menu()

#Name_SubMenu.choose()
