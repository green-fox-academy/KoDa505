import unittest
from menu import *

class TestMenu(unittest.TestCase):
    def test_exist(self):
        menu_item = MenuItem(1, "New game", "cmd")

    def test_name_number(self):
        menu_item = MenuItem(1, "New game", "cmd")
        self.assertEqual(menu_item.number, 1)
        self.assertEqual(menu_item.name, "New game")
        self.assertEqual(menu_item.cmd, "cmd")

    def test_listing(self):
        menulist = []
        menu_item2 = MenuItem(2, "Load game", "cmd")
        menu_item2.listing(menulist)
        self.assertEqual(menulist, [[2, "Load game", "cmd"]])

    def test_choose(self):
        menu_item = MenuItem(1, "New game", "cmd")
        return_cmd = menu_item.chosen([])
        self.assertEqual(return_cmd, "cmd")


unittest.main()
