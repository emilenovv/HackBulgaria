import random


class Fight:
    def __init__(self, fight_hero, fight_orc):
        self.fight_hero = fight_hero
        self.fight_orc = fight_orc

    def flip_coin(self):
        if random.random() < 0.5:
            return self.fight_hero
        else:
            return self.fight_orc

    def simulate_fight(self, fight_orc, fight_hero):
        if not self.fight_orc.has_weapon() and not self.fight_hero.has_weapon():
            return False
        elif self.flip_coin() == self.fight_hero:
            while self.fight_hero.is_alive() and self.fight_orc.is_alive():
                self.fight_orc.take_damage(self.fight_hero.attack())
                print("{} did {} damage to {}".format(self.fight_hero.name, self.fight_hero.attack(), self.fight_orc.name))
                self.fight_hero.take_damage(self.fight_orc.attack())
                print("{} did {} damage to {}".format(self.fight_orc.name, self.fight_orc.attack(), self.fight_hero.name))
            return True

        else:
            while self.fight_hero.is_alive() and self.fight_orc.is_alive():
                self.fight_hero.take_damage(self.fight_orc.attack())
                print("{} did {} damage to {}".format(self.fight_orc.name, self.fight_orc.attack(), self.fight_hero.name))
                self.fight_orc.take_damage(self.fight_hero.attack())
                print("{} did {} damage to {}".format(self.fight_hero.name, self.fight_hero.attack(), self.fight_orc.name))
            return True
        

