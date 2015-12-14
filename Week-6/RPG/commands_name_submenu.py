import commands
import quit_submenu
import random
import basic_elements
import reroll_submenu

def reenter_name():
    commands.new_game()

def continuing():
    d = random.randint(1,6)
    basic_elements.Player.dext = d + 6
    print("Your dexterity is: " + str(basic_elements.Player.dext))
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    basic_elements.Player.health = d1 + d2 + 12
    print("Your health is: " + str(basic_elements.Player.health))
    d = random.randint(1,6)
    basic_elements.Player.luck = d + 6
    print("Your luck is: " + str(basic_elements.Player.luck))
    reroll_submenu.Reroll_SubMenu.printing_menu()
    reroll_submenu.Reroll_SubMenu.choose()



def quitting():
    quit_submenu.Quit_SubMenu.printing_menu
    quit_submenu.Quit_SubMenu.choose
