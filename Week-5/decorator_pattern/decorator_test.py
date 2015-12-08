import unittest
from decorator import Gun


class GunTest(unittest.TestCase):
    def test_effect(self):
        weapon = Gun(TestWeapon())
        self.assertEqual(5, weapon.damage())

class TestWeapon:
    def damage(self):
        return 10

if __name__ == '__main__':
    unittest.main()
