import weapon
import unittest


class WeaponTest(unittest.TestCase):
    def setUp(self):
        self.magic_gun = weapon.Weapon("Gattling Gun", 15, 0.3)

    def test_weapon_init(self):
        self.assertEqual(self.magic_gun.type, "Gattling Gun")
        self.assertEqual(self.magic_gun.damage, 15)
        self.assertEqual(self.magic_gun.critical_strike_percent, 0.3)

    def test_weapon_critical_hit(self):
        results = []
        for i in range(100):
            results.append(self.magic_gun.critical_hit())
        self.assertTrue(True in results and False in results)


if __name__ == '__main__':
    unittest.main()