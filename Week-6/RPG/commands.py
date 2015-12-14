import menu
import name_submenu

def exiting():
    exit()

def new_game():
    name = input("Enter your name: ")
    print(name)
    name_submenu.Name_SubMenu.printing_menu()
    name_submenu.Name_SubMenu.choose()
