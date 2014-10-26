import entity
import unittest
from weapon import Weapon


class EntityTest(unittest.TestCase):
    def setUp(self):
        self.my_entity = entity.Entity("Galin", 100)

    def test_entity_init(self):
        self.assertEqual(self.my_entity.name, "Galin")
        self.assertEqual(self.my_entity.health, 100)

    def test_hero_get_max_health(self):
        self.assertEqual(self.my_entity.get_health(), 100)

    def test_hero_is_alive(self):
        self.assertTrue(self.my_entity.is_alive())
        self.my_entity.health = 0
        self.assertFalse(self.my_entity.is_alive())

    def test_hero_takes_damage(self):
        self.assertEqual(self.my_entity.take_damage(53), 47)

    def test_hero_takes_damage_more_than_health(self):
        self.assertEqual(self.my_entity.take_damage(120), 0)

    def test_dead_hero_takes_healing(self):
        self.my_entity.health = 0
        self.assertFalse(self.my_entity.take_healing(20))

    def test_above_max_health_hero_takes_healing(self):
        self.my_entity.health = 90
        self.assertTrue(self.my_entity.take_healing(20))
        self.assertEqual(self.my_entity.health, 100)

    def test_low_health_hero_takes_healing(self):
        self.my_entity.health = 20
        self.assertTrue(self.my_entity.take_healing(30))

    def test_has_no_weapon(self):
        self.assertFalse(self.my_entity.has_weapon())

    def test_equip_weapon(self):
        axe = Weapon("Mighty Axe", 25, 0.2)
        self.my_entity.equip_weapon(axe)
        self.assertEqual(self.my_entity.weapon, axe)

    def test_has_weapon(self):
        axe = Weapon("Mighty Axe", 25, 0.2)
        self.my_entity.weapon = axe
        self.assertTrue(self.my_entity.has_weapon())

    def test_attack_without_weapon(self):
        self.assertEqual(self.my_entity.attack(), 0)

    def test_attack_with_weapon(self):
        axe = Weapon("Mighty Axe", 25, 0.2)
        self.my_entity.weapon = axe
        self.assertEqual(self.my_entity.attack(), 25)

    def test_attack_when_weapon_crits(self):
        axe = Weapon("Mighty Axe", 25, 1)
        self.my_entity.weapon = axe
        self.assertEqual(self.my_entity.attack(), 50)

if __name__ == '__main__':
    unittest.main()