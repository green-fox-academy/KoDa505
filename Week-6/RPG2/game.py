import menu_list
import player


class Game():
    def __init__(self):
        self.menu = menu_list.Main_Menu()
        self.player = player.Player()

    def start(self):
        self.menu.printing_menu()

game1 = Game()

game1.start()
