import orc
import unittest
from weapon import Weapon

class OrcTest(unittest.TestCase):
    def setUp(self):
        self.bad_orc = orc.Orc("Haguk", 100, 1.4)

    def test_orc_init(self):
        self.assertEqual(self.bad_orc.name, "Haguk")
        self.assertEqual(self.bad_orc.health, 100)
        self.assertEqual(self.bad_orc.berserk_factor, 1.4)

    def test_orc_berserk_out_of_bounds_more(self):
        max_orc = orc.Orc("Haguk", 100, 5)
        self.assertEqual(max_orc.berserk_factor, 2)

    def test_orc_berserk_out_of_bounds_less(self):
        less_orc = orc.Orc("Haguk", 100, 0)
        self.assertEqual(less_orc.berserk_factor, 1)

    def test_orc_damage(self):
        axe = Weapon("Mighty Axe", 15, 0.2)
        self.bad_orc.weapon = axe
        self.assertEqual(self.bad_orc.attack(), 21)

if __name__ == '__main__':
    unittest.main()

