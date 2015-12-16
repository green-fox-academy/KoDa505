import commands
import basic_elements
import reroll_submenu
import class_Player

def reenter_name():
    commands.Commands_MainMenu.new_game()

def continuing():
    class_Player.player1.shuffle_properties()
    class_Player.player1.display_print()
    reroll_submenu.Reroll_SubMenu.printing_menu()
    reroll_submenu.Reroll_SubMenu.choose()

def save():
    pass

def quitting():
    commands.quitting()
