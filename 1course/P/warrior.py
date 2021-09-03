from abc import ABCMeta, abstractmethod
from random import randint as ri

units_classes = {"MAGICIAN": "MAGICAL", "WARRIOR": "SIMPLE"}


class Unit:
    max_health = 0
    __metaclass__ = ABCMeta
    _max_damage = 0
    _block_chance = (0, 0, 0)  # randint([0], [1])==[2]

    @abstractmethod
    def __init__(self, name, health=max_health):
        self.name = name
        self.health = health

    @abstractmethod
    def hit(self, other):
        damage = ri(1, self._max_damage)
        if ri(self._block_chance[0], self._block_chance[1]) == self._block_chance[2]:
            other.health -= damage
            print(f"Action:{other.name} took {damage} {units_classes[self.name.split()[1]]} damage from {self.name}")
        else:
            print(f"Action:{other.name} BLOCKED {damage} {units_classes[self.name.split()[1]]} damage from {self.name}")
        return damage


class Warrior(Unit):
    max_health = 100
    _max_damage = 100
    _block_chance = (0, 2, 0)

    def __init__(self, name, health=max_health):
        super().__init__(name, health)

    def hit(self, other):
        super().hit(other)


class Magician(Unit):  # have a large damage
    max_health = 90
    _max_damage = 50
    _block_chance = (0, 1, 0)

    def __init__(self, name, health=max_health):
        super().__init__(name, health)

    def hit(self, other):
        super().hit(other)
        # print(f"Action:{other.name} took {damage} MAGICAL damage from {self.name}")


class KlirikBeginner(Unit):  # can make a oneshot or heal opponent to full hp
    max_health = 200

    def __init__(self, name, health=max_health):
        super().__init__(name, health)

    def hit(self, other):
        damage = other.health if ri(0, 50) == 1 else -other.max_health + other.health
        other.health -= damage
        if damage > 0:
            print(f"Action: {other.name} took {damage} KLIRIKAL damage from {self.name}")
        else:
            print(f"Action:{other.name} HEALED to {-damage} by {self.name}")


def team_generator(quantity, team_name):
    players = []
    for i in range(quantity):
        rand_cls_chooser = ri(1, 100)
        if 1 < rand_cls_chooser < 20:
            players.append(Magician(f"[{team_name}] MAGICIAN {i}"))
        elif 20 < rand_cls_chooser < 30:
            players.append(KlirikBeginner(f"[{team_name}] KLIRIK {i}"))
        elif 30 < rand_cls_chooser < 100:
            players.append(Warrior(f"[{team_name}] WARRIOR {i}"))
    return players


def death_checker(inst):
    return inst.health <= 0


class Game:
    def __init__(self, teams_list):
        self.teams_list = teams_list

    def battle(self):
        while len(self.teams_list) > 1:
            t1_index, t2_index = ri(0, len(self.teams_list) - 1), ri(0, len(self.teams_list) - 1)
            if t1_index != t2_index:
                team1, team2 = self.teams_list[t1_index], self.teams_list[t2_index]
                p1_t1_index, p2_t2_index = ri(0, len(team1) - 1), ri(0, len(team2) - 1)
                player1, player2 = team1[p1_t1_index], team2[p2_t2_index]
                player1.hit(player2)
                if death_checker(player2):
                    print(f"######### Player {player2.name} DEAD #########")
                    self.teams_list[t2_index].pop(p2_t2_index)
                else:
                    player2.hit(player1)
                    if death_checker(player1):
                        print(f"######### Player {player1.name} DEAD #########")
                        self.teams_list[t1_index].pop(p1_t1_index)
                if not self.teams_list[t1_index]:
                    self.teams_list.pop(t1_index)
                elif not self.teams_list[t2_index]:
                    self.teams_list.pop(t2_index)
        return self.teams_list[0][0].name.split()[0]


if __name__ == "__main__":
    team1 = team_generator(100, "GaYs")
    team2 = team_generator(100, "SlAvEs")
    team3 = team_generator(100, "MuRaT")
    team4 = team_generator(100, "kFu")
    teams = [team1, team2, team3, team4]
    # fight = Game([team1, team2, team3, team4])

    # teams = [team_generator(2, i) for i in range(100)]  # not working with (1, i)
    fight = Game(teams)
    print(f"Winner: {fight.battle()}")
