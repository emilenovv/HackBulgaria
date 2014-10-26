from weapon import Weapon

class Entity:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.max_health = health
        self.weapon = None

    def get_health(self):
        return self.health

    def is_alive(self):
        return self.get_health() > 0

    def take_damage(self, damage):
        if damage > self.get_health():
            self.health = 0
        else:
            self.health -= damage
        return self.get_health()

    def take_healing(self, healing_points):
        if not self.is_alive():
            return False
        if self.health + healing_points > self.max_health:
            self.health = self.max_health
        else:
            self.health += healing_points
        return True

    def equip_weapon(self, weapon):
        self.weapon = weapon

    def has_weapon(self):
        if self.weapon == None:
            return False
        else:
            return True

    def attack(self):
        if not self.has_weapon():
            return 0
        else:
            if self.weapon.critical_hit():
                return 2 * self.weapon.damage
            else:
                return self.weapon.damage
