import basic_elements
import name_submenu
import quit_submenu



def exiting():
    exit()

def new_game():
    name = input("Enter your name: ")
    print(name)
    name_submenu.Name_SubMenu.printing_menu()
    name_submenu.Name_SubMenu.choose()
    basic_elements.player1.name = name
    return name


def save():
    pass

def quitting():
    quit_submenu.Quit_SubMenu.printing_menu()
    quit_submenu.Quit_SubMenu.choose()
