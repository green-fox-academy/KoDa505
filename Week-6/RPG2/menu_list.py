from menu import MenuItem


class Main_Menu(MenuItem):
    def __init__(self):
        super().__init__()
        self.create_menu(New_game(1, "New game", apply))
        self.create_menu(Load_game(2, "Load game", "cmd"))
        self.create_menu(Exit(3, "Exit", "cmd"))


class New_game(MenuItem):
    def __init__(self):
        super().__init__()
    def apply(player):
        name = input("Enter your name: ")
        player.name = name
        player.display_print()
        Name_Menu.printing_menu()
        Name_Menu.choose()
        return name

class Load_game(MenuItem):
    pass

class Exit(MenuItem):
    pass

class Name_Menu(MenuItem):
    def __init__(self):
        super().__init__()
        self.create_menu(Reenter_name(1, "Reenter name", commands_name_submenu.reenter_name))
        self.create_menu(Continue_Name(2, "Continue", commands_name_submenu.continuing))
        self.create_menu(Save_Name(3, "Save", commands_name_submenu.save))
        self.create_menu(Quit(4, "Quit", commands_name_submenu.quitting))

class Reenter_name(MenuItem):
    def __init__(self):
        super().__init__()

class Continue_Name(MenuItem):
    def __init__(self):
        super().__init__()

class Save_Name(MenuItem):
    def __init__(self):
        super().__init__()

class Quit(MenuItem):
    def __init__(self):
        super().__init__()
        self.create_menu(Save_and_Quit(1, "Save and Quit", "sfhoi"))
        self.create_menu(Quit_without_save(2, "Quit without save", exiting))
        self.create_menu(Resume(3, "Resume", "save function"))

class Save_and_Quit(MenuItem):
    def __init__(self):
        super().__init__()


class Quit_without_save(MenuItem):
    def __init__(self):
        super().__init__()

class Resume(MenuItem):
    def __init__(self):
        super().__init__()

class Reroll_Menu(MenuItem):
    def __init__(self):
        super().__init__()
        self.create_menu(Reroll_stats(1, "Reroll stats", f))
        self.create_menu(Continue_Reroll(2, "Continue", f))
        self.create_menu(Save_Reroll(3, "Save", f))
        self.create_menu(Quit(4, "Quit", f))

class Reroll_stats(MenuItem):
    def __init__(self):
        super().__init__()

class Continue_Reroll(MenuItem):
    def __init__(self):
        super().__init__()

class Save_Reroll(MenuItem):
    def __init__(self):
        super().__init__()
