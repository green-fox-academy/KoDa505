from basic_elements import *
import commands
import commands_name_submenu
import potion_submenu



def reroll():
    commands_name_submenu.continuing()

def create_reselect():
    Reselect_Potion_SubMenu = Menu()
    Menu1 = MenuItem(1, "Reselect potion", continuing)
    Menu2 = MenuItem(2, "Continue", "kuigig")
    Menu3 = MenuItem(3, "Quit", "sagaegt")
    Reselect_Potion_SubMenu.add(Menu1)
    Reselect_Potion_SubMenu.add(Menu2)
    Reselect_Potion_SubMenu.add(Menu3)
    Reselect_Potion_SubMenu.printing_menu()
    Reselect_Potion_SubMenu.choose()

def continuing():
    potion_submenu.Potion_SubMenu.printing_menu()
    potion_submenu.Potion_SubMenu.choose_print()
    create_reselect()

def save():
    pass

def quitting():
    commands.quitting()
