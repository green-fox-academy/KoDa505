
class Menu():
    def __init__(self):
        self.items = []

    def printing_menu(self):
        for item in self.items:
            print("\n" + str(item.number) + ". " + str(item.name) + "\n" + "----"*10)

    def add(self, item):
        self.items.append(item)


    def choice_input(self):
        while True:
            try:
                choice_number = int(input("Enter the number of your choice: "))
                if choice_number > len(self.items):
                    print('out of range')
                else:
                    return choice_number
            except ValueError:
                print("incorrect input")

    def select_item(self, choice_number):
        for item in self.items:
            if choice_number == item.number:
                return item

    def choose_item(self):
        choice_number = self.choice_input()
        return self.select_item(choice_number)

    def choose(self):
        self.choose_item().cmd()

    def choose_print(self):
        print(self.choose_item().name)


class MenuItem():
    def __init__(self, number, name, cmd):
        self.name = name
        self.number = number
        self.cmd = cmd
