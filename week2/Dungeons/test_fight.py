import fight
import unittest
import hero
import orc
import weapon


class FightTest(unittest.TestCase):
    def setUp(self):
        black_orc = orc.Orc("Cho_gath", 150, 1.2)
        white_hero   = hero.Hero("Jinx", 150, "Loose Cannon")
        self.arena = fight.Fight(white_hero, black_orc)

    def test__fight__init(self):
        self.assertEqual(self.arena.fight_orc.name, "Cho_gath")
        self.assertEqual(self.arena.fight_orc.health, 150)
        self.assertEqual(self.arena.fight_orc.berserk_factor, 1.2)
        self.assertEqual(self.arena.fight_hero.name, "Jinx")
        self.assertEqual(self.arena.fight_hero.health, 150)
        self.assertEqual(self.arena.fight_hero.nickname, "Loose Cannon")

    def test_flip_coin(self):
        results = []
        for i in range(10):
            results.append(self.arena.flip_coin())
        self.assertTrue(self.arena.fight_orc in results and self.arena.fight_hero in results)

    def test_simulate_fight(self):
        sniper = weapon.Weapon("Sniper Rifle", 12, 0.6)
        sword = weapon.Weapon("Magic Sword", 10, 0.7)
        self.arena.fight_orc.weapon = sword
        self.arena.fight_hero.weapon = sniper
        self.arena.simulate_fight(self.arena.fight_hero, self.arena.fight_orc)
        self.assertTrue(not self.arena.fight_orc.is_alive() or not self.arena.fight_hero.is_alive())

    def test_simulate_fight_one_without_gun(self):
        sniper = weapon.Weapon("Sniper Rifle", 12, 0.6)
        self.arena.fight_hero.weapon = sniper
        self.assertFalse(self.arena.fight_orc.has_weapon())
        self.arena.simulate_fight(self.arena.fight_orc, self.arena.fight_hero)
        self.assertFalse(self.arena.fight_orc.is_alive())

    def test_fight_no_one_has_weapon(self):
        self.assertEqual(self.arena.simulate_fight(self.arena.fight_orc, self.arena.fight_hero),
        "Both of you have no weapon. Go and grab a gun")

if __name__ == '__main__':
    unittest.main()
