import commands
import random
import basic_elements
import reroll_submenu

def reenter_name():
    commands.new_game()

def continuing():
    d = random.randint(1,6)
    basic_elements.player1.dexterity = d + 6
    print("Your dexterity is: " + str(basic_elements.player1.dexterity))
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    basic_elements.player1.health = d1 + d2 + 12
    print("Your health is: " + str(basic_elements.player1.health))
    d = random.randint(1,6)
    basic_elements.player1.luck = d + 6
    print("Your luck is: " + str(basic_elements.player1.luck))
    reroll_submenu.Reroll_SubMenu.printing_menu()
    reroll_submenu.Reroll_SubMenu.choose()

def save():
    pass

def quitting():
    commands.quitting()
