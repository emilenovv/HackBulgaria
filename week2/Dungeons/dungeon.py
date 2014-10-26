import random


from hero import Hero
from orc import Orc
from weapon import Weapon
from entity import Entity


class Dungeon:
    def __init__(self, path):
        self.path = path
        self.source = open(self.path, "r")
        self.raw_file = self.source.readlines()
        self.content = []
        for i in range(self.end_of_map_finder()):
            self.content.append(self.raw_file[i])
        self.weapons_file = []
        for i in range(self.end_of_map_finder() + 1, len(self.raw_file)):
            self.weapons_file.append(self.raw_file[i])
        self.hero_player_name = None
        self.orc_player_name = None
        self.hero_player = None
        self.orc_player = None
        self.available_weapons = []
        self.parse_weapons()

    def print_map(self):
        print(self.content)
        for line in self.content:
            print(line)
        self.source.close()

    def spawn(self, player_name, entity):
        for index in range(len(self.content)):
            for char in self.content[index]:
                if char == "S":
                    if isinstance(entity, Hero):
                        self.hero_player = entity
                        self.hero_player_name = player_name
                        self.content[index] = self.content[index].replace(char, "H", 1)
                        return True
                    if isinstance(entity, Orc):
                        self.orc_player = entity
                        self.orc_player_name = player_name
                        self.content[index] = self.content[index].replace(char, "O", 1)
                        return True
        return False

    def move_up(self, player_name):
        for index_of_line in range(len(self.content)):
            for index_of_char in range(len(self.content[index_of_line])):
                if player_name == self.hero_player_name and self.content[index_of_line][index_of_char] in "H" or player_name == self.orc_player_name and self.content[index_of_line][index_of_char] in "O":
                    if self.content[index_of_line - 1][index_of_char] == '.':
                        self.content[index_of_line][index_of_char], self.content[index_of_line - 1][index_of_char] = self.content[index_of_line - 1][index_of_char], self.content[index_of_line][index_of_char]
                        return True
                    elif self.content[index_of_line - 1][index_of_char] == "W":
                        self.content[index_of_line][index_of_char] = "."
                        if player_name == self.hero_player_name:
                            self.pick_up_weapon(self.hero_player)
                            self.content[index_of_line - 1][index_of_char] = "H"
                        elif player_name == self.orc_player_name:
                            self.pick_up_weapon(self.orc_player)
                            self.content[index_of_line - 1][index_of_char] = "O"
                            return True
                    elif self.content[index_of_line][index_of_char] == "H":
                        if self.content[index_of_line - 1][index_of_char] == "O":
                            pass
                    elif self.content[index_of_line][index_of_char] == "O":
                        if self.content[index_of_line - 1][index_of_char] == "H":
                            pass

    def move_down(self, player_name, size_lines):
        print("down")
        for index_of_line in range(len(self.content)):
            for index_of_char in range(len(self.content[index_of_line])):
                if player_name == self.hero_player_name and self.content[index_of_line][index_of_char] in "H" or player_name == self.orc_player_name and self.content[index_of_line][index_of_char] in "O":
                    if index_of_line + 1 >= size_lines:
                        return False
                    elif self.content[index_of_line + 1][index_of_char] == '.':
                        self.content[index_of_line][index_of_char], self.content[index_of_line + 1][index_of_char] = self.content[index_of_line + 1][index_of_char], self.content[index_of_line][index_of_char]
                        return True
                    elif self.content[index_of_line + 1][index_of_char] == "W":
                        self.content[index_of_line][index_of_char] = "."
                        if player_name == self.hero_player_name:
                            self.pick_up_weapon(self.hero_player)
                            self.content[index_of_line + 1][index_of_char] = "H"
                        elif player_name == self.orc_player:
                            self.pick_up_weapon(self.orc_player)
                            self.content[index_of_line + 1][index_of_char] = "O"
                        return True
                    elif self.content[index_of_line][index_of_char] == "H":
                        if self.content[index_of_line + 1][index_of_char] == "O":
                            pass
                    elif self.content[index_of_line][index_of_char] == "O":
                        if self.content[index_of_line + 1][index_of_char] == "H":
                            pass

    def move_left(self, player_name):
        for index_of_line in range(len(self.content)):
            for index_of_char in range(len(self.content[index_of_line])):
                if player_name == self.hero_player_name and self.content[index_of_line][index_of_char] in "H" or player_name == self.orc_player_name and self.content[index_of_line][index_of_char] in "O":
                    if self.content[index_of_line][index_of_char - 1] == '.':
                        self.content[index_of_line][index_of_char], self.content[index_of_line][index_of_char - 1] = self.content[index_of_line][index_of_char - 1], self.content[index_of_line][index_of_char]
                        return True
                    elif self.content[index_of_line][index_of_char - 1] == "W":
                        self.content[index_of_line][index_of_char] = "."
                        if player_name == self.hero_player_name:
                            self.pick_up_weapon(self.hero_player)
                            self.content[index_of_line][index_of_char - 1] = "H"
                        elif player_name == self.orc_player_name:
                            self.pick_up_weapon(self.orc_player)
                            self.content[index_of_line][index_of_char - 1] = "O"
                        return True
                    elif self.content[index_of_line][index_of_char] == "H":
                        if self.content[index_of_line][index_of_char - 1] == "O":
                            pass
                    elif self.content[index_of_line][index_of_char] == "O":
                        if self.content[index_of_line][index_of_char - 1] == "H":
                            pass

    def move_right(self, player_name, size_cols):
        for index_of_line in range(len(self.content)):
            for index_of_char in range(len(self.content[index_of_line])):
                if player_name == self.hero_player_name and self.content[index_of_line][index_of_char] in "H" or player_name == self.orc_player_name and self.content[index_of_line][index_of_char] in "O":
                    if index_of_char + 1 >= size_cols:
                        return False
                    elif self.content[index_of_line][index_of_char + 1] == '.':
                        self.content[index_of_line][index_of_char], self.content[index_of_line][index_of_char + 1] = self.content[index_of_line][index_of_char + 1], self.content[index_of_line][index_of_char]
                        return True
                    elif self.content[index_of_line][index_of_char + 1] == "W":
                        self.content[index_of_line][index_of_char] = "."
                        if player_name == self.hero_player_name:
                            self.pick_up_weapon(self.hero_player)
                            self.content[index_of_line][index_of_char + 1] = "H"
                        elif player_name == self.orc_player_name:
                            self.pick_up_weapon(self.orc_player)
                            self.content[index_of_line][index_of_char + 1] = "O"
                        return True
                    elif self.content[index_of_line][index_of_char] == "H":
                        if self.content[index_of_line][index_of_char + 1] == "O":
                            pass
                    elif self.content[index_of_line][index_of_char] == "O":
                        if self.content[index_of_line][index_of_char + 1] == "H":
                            pass

    def move(self, player_name, direction):
        size_lines = len(self.content)
        size_cols = len(self.content[0])
        for index in range(len(self.content)):
            self.content[index] = list(self.content[index])
        if direction == "up":
            self.move_up(player_name)
        elif direction == "down":
            self.move_down(player_name, size_lines)
        elif direction == "left":
            self.move_left(player_name)
        elif direction == "right":
            self.move_right(player_name, size_cols)
        else:
            return "Please select ..."
        for index in range(len(self.content)):
            self.content[index] = "".join(self.content[index])

    def spawn_weapons(self):
        dots_list = []
        for index_of_line in range(len(self.content)):
            self.content[index_of_line] = list(self.content[index_of_line])
            for index_of_char in range(len(self.content[index_of_line])):
                if self.content[index_of_line][index_of_char] == '.':
                    dots_list.append(tuple([index_of_line, index_of_char]))
        for i in range(2):
            spawn_tuple = dots_list[random.randrange(0, len(dots_list))]
            spawn_line = spawn_tuple[0]
            spawn_col = spawn_tuple[1]
            #self.content[spawn_line][spawn_col] = "W"
            self.content[2][1] = "W"
            self.content[2][9] = "W"
        self.from_list_to_matrix()

    def end_of_map_finder(self):
        index = 0
        for line in self.raw_file:
            if line == "\n":
                break
            index += 1
        return index

    def parse_weapons(self):
        for i in range(len(self.weapons_file)):
            self.weapons_file[i] = self.weapons_file[i].split()
            self.available_weapons.append(Weapon(self.weapons_file[i][0], self.weapons_file[i][1], self.weapons_file[i][2]))
        print("Guns", self.weapons_file)
        return self.available_weapons

    def pick_up_weapon(self, entity):
        print("Emil", len(self.available_weapons))
        if len(self.available_weapons) == 0:
            return "There are no more weapons"
        i = random.randrange(len(self.available_weapons))
        entity.equip_weapon(self.available_weapons[i])
        self.available_weapons.remove(self.available_weapons[i])
        print("Weapon equipped!")
        return True

    def from_list_to_matrix(self):
        for index in range(len(self.content)):
            self.content[index] = "".join(self.content[index])
        return self.content
