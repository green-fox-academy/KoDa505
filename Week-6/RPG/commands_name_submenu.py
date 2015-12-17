import commands
import basic_elements
import reroll_submenu
import player

def reenter_name():
    commands.Commands_MainMenu.new_game()

def continuing():
    player.player1.shuffle_properties()
    player.player1.display_print()
    reroll_submenu.Reroll_SubMenu.printing_menu()
    reroll_submenu.Reroll_SubMenu.choose()

def save():
    pass

def quitting():
    commands.quitting()
