import dungeon
import orc
import hero
import unittest


class DungeonTest(unittest.TestCase):
    def setUp(self):
        self.summoners_rift = dungeon.Dungeon("Sample_rift.txt")

    def test_dungeon_init(self):
        self.assertEqual(self.summoners_rift.path, "Sample_rift.txt")

    def test_spawn_hero(self):
        jax = hero.Hero("Jax", 150, "Killer")
        self.assertTrue(self.summoners_rift.spawn("Galin", jax))
        urgot = orc.Orc("Urgot", 200, 1.6)
        self.assertTrue(self.summoners_rift.spawn("Emil", urgot))
        sion = orc.Orc("Sion", 432, 2.6)
        self.assertFalse(self.summoners_rift.spawn("Sion", sion))

    def test_move(self):
        jax = hero.Hero("Jax", 150, "Killer")
        self.summoners_rift.spawn("Galin", jax)
        self.summoners_rift.move("Galin", "right")
        self.summoners_rift.move("Galin", "down")
        self.summoners_rift.move("Galin", "down")
        #self.summoners_rift.move("Galin", "down")
        urgot = orc.Orc("Emil", 200, 1.6)
        self.summoners_rift.spawn("Emil", urgot)
        self.summoners_rift.move("Emil", "up")

    def test_spawn_weapons(self):
        self.summoners_rift.spawn_weapons()
        jax = hero.Hero("Jax", 150, "Killer")
        self.summoners_rift.spawn("Galin", jax)
        self.summoners_rift.move("Galin", "right")
        self.summoners_rift.move("Galin", "down")
        self.summoners_rift.move("Galin", "down")
        urgot = orc.Orc("Emil", 200, 1.6)
        self.summoners_rift.spawn("Emil", urgot)
        self.summoners_rift.move("Emil", "up")
        self.summoners_rift.move("Emil", "up")

    def test_fight_in_dungeon(self):
        jax = hero.Hero("Jax", 3000, "Killer")
        urgot = orc.Orc("Emil", 2000, 1.3)
        self.summoners_rift.spawn("Galin", jax)
        self.summoners_rift.spawn("Emil", urgot)
        self.summoners_rift.move("Galin", "right")
        self.summoners_rift.move("Galin", "down")
        self.summoners_rift.move("Galin", "down")
        self.summoners_rift.move("Emil", "left")
        self.summoners_rift.move("Galin", "down")
        self.summoners_rift.print_map()



if __name__ == '__main__':
    unittest.main()