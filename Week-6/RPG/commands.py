import class_Player
import basic_elements
import name_submenu
import quit_submenu



class Commands_MainMenu:
    def exiting():
        exit()

    def new_game():
        name = input("Enter your name: ")
        print(name)
        class_Player.player1.name = name
        class_Player.player1.display_print()
        name_submenu.Name_SubMenu.printing_menu()
        name_submenu.Name_SubMenu.choose()
        return name


    def save():
        pass

    def quitting():
        quit_submenu.Quit_SubMenu.printing_menu()
        quit_submenu.Quit_SubMenu.choose()
