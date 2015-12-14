import basic_elements
import name_submenu



def exiting():
    exit()

def new_game():
    basic_elements.Player.name = input("Enter your name: ")
    print(basic_elements.Player.name)
    name_submenu.Name_SubMenu.printing_menu()
    name_submenu.Name_SubMenu.choose()
