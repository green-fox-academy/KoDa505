import main_menu
import basic_elements
import name_submenu
import reroll_submenu
import quit_submenu
import potion_submenu
import player



class Game:
    def start_game(self):
        main_menu.MainMenu.printing_menu()
        main_menu.MainMenu.choose()
        return



game1 = Game()

game1.start_game()

player.player1.display_print()
