import unittest
from basic_elements import *

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
        def test_func():
            return True
        menu_item = MenuItem(1, "New game", test_func)
        self.assertEqual(menu_item.choose(), "kacsa")


unittest.main()
