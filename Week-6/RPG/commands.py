import player
import basic_elements
import name_submenu
import quit_submenu



class Commands_MainMenu:
    def exiting():
        exit()

    def new_game():
        name = input("Enter your name: ")
        player.player1.name = name
        player.player1.display_print()
        name_submenu.Name_SubMenu.printing_menu()
        name_submenu.Name_SubMenu.choose()
        return name


    def save():
        pass

    def quitting():
        quit_submenu.Quit_SubMenu.printing_menu()
        quit_submenu.Quit_SubMenu.choose()
