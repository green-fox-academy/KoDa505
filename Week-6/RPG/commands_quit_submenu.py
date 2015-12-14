import commands
import quit_submenu

def reenter_name():
    commands.new_game()

def continuing():
    pass

def quitting():
    quit_submenu.Quit_SubMenu.printing_menu
    quit_submenu.Quit_SubMenu.choose
