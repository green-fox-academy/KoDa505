class MenuItem():
    def __init__(self, number=0, name='', cmd=None):
        self.name = name
        self.number = number
        self.cmd = cmd
        self.items = []


    def create_menu(self, item):
        self.items.append(item)

    def printing_menu(self):
        for item in self.items:
            print("\n" + str(item.number) + ". " + str(item.name) + "\n" + "----"*10)

    def apply_item(self, player):
        return self.cmd(player)
