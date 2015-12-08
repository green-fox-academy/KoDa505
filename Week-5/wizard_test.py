import unittest
from wizard import Wizard

class TestWizard(unittest.TestCase):
    def test_existance(self):
        wizard = Wizard('Merlin', 40, 10, 20)

    def test_inheritance(self):
        wizard = Wizard('Merlin', 40, 10, 20)
        self.assertEqual(wizard.hp, 40)

    def test_manna(self):
        wizard = Wizard('Merlin', 40, 10, 20)
        self.assertEqual(wizard.manna, 20)

    def test_strike_manna_decrease(self):
        wizard = Wizard('Merlin', 40, 10, 20)
        opponent = Wizard('Oz', 40, 10, 30)
        wizard.strike(opponent)
        self.assertEqual(wizard.manna, 15)

    def test_strike_triple_damage(self):
        wizard = Wizard('Merlin', 40, 10, 20)
        opponent = Wizard('Oz', 40, 10, 30)
        wizard.strike(opponent)
        self.assertEqual(wizard.manna, 15)
        self.assertEqual(opponent.hp, 10)

    def test_strike_too_less_manna(self):
        wizard = Wizard('Merlin', 40, 12, 4)
        opponent = Wizard('Oz', 40, 10, 30)
        wizard.strike(opponent)
        self.assertEqual(wizard.manna, 4)
        self.assertEqual(opponent.hp, 36)






unittest.main()
