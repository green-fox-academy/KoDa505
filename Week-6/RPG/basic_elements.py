class Menu():
    def __init__(self):
        self.items = []

    def printing_menu(self):
        for item in self.items:
            print(str(item[0]) + ". " + str(item[1]))

    def add(self, item):
        self.items.append(item)

    def choose(self):
        while True:
            try:
                choice_number = int(input("Enter the number of your choice: "))
            except ValueError:
                print("incorrect input")
            else:
                if choice_number > len(self.items):
                    print('out of range')
                else:
                    for item in self.items:
                        if choice_number == item[0]:
                            return item[2]()
                    break

class MenuItem():
    def __init__(self, number, name, cmd):
        self.name = name
        self.number = number
        self.cmd = cmd
        self.item = [self.number, self.name, self.cmd]
