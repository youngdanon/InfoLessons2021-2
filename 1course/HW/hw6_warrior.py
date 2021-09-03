from random import randint, choice, choices
import copy
from colorama import Fore, Back, Style


def chance(a):
    return choices([True, False], [a, 1 - a])[0]


class Warrior:
    def __init__(self, name="No name", max_hp=100, race="Не указана",
                 gender="Не указано", slope_prob=0, buff_scale=1):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.race = race
        self.gender = gender
        self.dodge_prob = slope_prob
        self.buff_scale = buff_scale

    def attack(self, player, min_dmg, max_dmg):
        damage = randint(min_dmg, max_dmg)
        if not player.dodge_chance():
            player.hp -= damage
            print(f"Action: {player.name} took {damage} damage from {self.name}")
        else:
            print(f"{player.name} blocked {damage} damage from {self.name}")

    def dodge_chance(self):
        return choices([True, False], [self.dodge_prob, 1 - self.dodge_prob])[0]

    def bio(self):
        print(f'###### Воин "{self.name}" ######',
              f'Race: {self.race}',
              f'Gender: {self.gender}',
              f'HP: {self.hp}/{self.max_hp}',
              f'Dodge (blocking) probability: {self.dodge_prob}',
              '-' * (19 + len(self.name)), sep="\n")


class Human(Warrior):
    def __init__(self, name="No name", max_hp=100, w_class="Без класса",
                 gender="Не указан", slope_prob=0, buff_scale=1):
        super().__init__(name, max_hp, F"Человек ({w_class})", gender, slope_prob, buff_scale)
        self.dodge_prob *= buff_scale


class Orc(Warrior):
    def __init__(self, name="No name", max_hp=100, w_class="Без класса",
                 gender="Не указан", slope_prob=0, buff_scale=1):
        super().__init__(name, max_hp, F"Орк ({w_class})", gender, slope_prob, buff_scale)

    def attack(self, player, min_dmg, max_dmg):
        super().attack(player, min_dmg * self.buff_scale, max_dmg * self.buff_scale)


class Light(Human):
    def __init__(self, name="No name", gender="Не указано", buff_scale=1):
        super().__init__(name, 200, "Легкая пехота", gender, 0.3, buff_scale)

    def attack(self, player):
        super().attack(player, 30, 50)


class Heavy(Human):
    def __init__(self, name="No name", gender="Не указано", buff_scale=1):
        super().__init__(name, 500, "Тяжелая пехота", gender, 0, buff_scale)

    def attack(self, player):
        super().attack(player, 50, 70)


class Druid(Human):
    def __init__(self, name="No name", gender="Не указано", buff_scale=1):
        super().__init__(name, 100, "Друид", gender, 0.7, buff_scale)

    def attack(self, player):
        if not isinstance(player, Shaman):
            player.hp = 10
            print(f"Action: Druid {self.name} infected {player.name}")

    def heal(self, player):
        if not isinstance(player, Druid):
            player.hp = player.max_hp
            print(f"Action: Druid {self.name} healed {player.name}")


class Berserker(Orc):
    def __init__(self, name="No name", gender="Не указано", buff_scale=1):
        super().__init__(name, 600, "Берсерк", gender, 0.1, buff_scale)

    def attack(self, player):
        super().attack(player, 60, 90)


class Shaman(Orc):
    def __init__(self, name="No name", gender="Не указано", buff_scale=1):
        super().__init__(name, 120, "Шаман", gender, 0.7, buff_scale)

    def attack(self, player):
        if not isinstance(player, Druid):
            player.hp = 10
            print(f"Action: Shaman {self.name} infected {player.name}")

    def heal(self, player):
        if not isinstance(player, Shaman):
            player.hp = player.max_hp
            print(f"Action: Shaman {self.name} healed {player.name}")


class Army:
    def __init__(self, name="Unnamed army", light=0, heavy=0, druid=0, berserk=0, shaman=0):
        self.name = name
        self.warriors = []
        gender_choice = lambda: choice(["Мужской, женский"])
        self.warriors += [Light(f"[{name}] Light{i}", gender_choice()) for i in range(light)]
        self.warriors += [Heavy(f"[{name}] Heavy{i}", gender_choice()) for i in range(heavy)]
        self.warriors += [Druid(f"[{name}] Druid{i}", gender_choice()) for i in range(druid)]
        self.warriors += [Berserker(f"[{name}] Berserk{i}", gender_choice()) for i in range(berserk)]
        self.warriors += [Shaman(f"[{name}] Shaman{i}", gender_choice()) for i in range(shaman)]

    def warrior_death(self, warrior):
        self.warriors.remove(warrior)

    def attack(self, opp_army):
        warrior: Warrior = choice(self.warriors)
        opp_warrior: Warrior = choice(opp_army.warriors)
        if not isinstance(warrior, (Druid, Shaman)):
            warrior.attack(opp_warrior)
            if opp_warrior.hp <= 0:
                print(f"{Fore.YELLOW}========Action: {warrior.name} KILLED {opp_warrior.name}========")
                print(Style.RESET_ALL, end="")
                opp_army.warrior_death(opp_warrior)
        elif isinstance(warrior, Druid):
            if choices([True, False], [0.3, 0.7])[0]:
                warrior.attack(opp_warrior)
                if opp_warrior.hp <= 0:
                    print(f"{Fore.YELLOW}========Action: {warrior.name} KILLED {opp_warrior.name}========")
                    print(Style.RESET_ALL, end="")
                    opp_army.warrior_death(opp_warrior)
            else:
                warrior.heal(choice(self.warriors))

        elif isinstance(warrior, Shaman):
            if choice([True, False]):
                warrior.attack(opp_warrior)
                if opp_warrior.hp <= 0:
                    print(f"========Action: {warrior.name} KILLED {opp_warrior.name}========")
                    opp_army.warrior_death(opp_warrior)
            else:
                warrior.heal(choice(self.warriors))


class Battle:
    def __init__(self, humans_team: Army, orcs_team, index=None):
        self.humans_team, self.orcs_team = copy.deepcopy(humans_team), copy.deepcopy(orcs_team)
        self.winner = None
        self.start_flag = False
        self.idx = index

    def start(self):
        self.start_flag = True
        print("++++++++++ БИТВА НАЧАЛАСЬ ++++++++++")
        while True:
            if self.orcs_team.warriors:
                self.orcs_team.attack(self.humans_team)
            else:
                self.winner = self.humans_team.name
                break
            if self.humans_team.warriors:
                self.humans_team.attack(self.orcs_team)
            else:
                self.winner = self.orcs_team.name
                break

    def __del__(self):
        if self.start_flag:
            print(f"{Fore.CYAN}++++++++++ БИТВА {self.idx} ЗАВЕРШЕНА ПОБЕДОЙ <<{self.winner}>> ++++++++++")
            print(Style.RESET_ALL, end="")

        else:
            raise Exception("Вы не запустили битву командой start()")


if __name__ == "__main__":
    humans_team = Army("Команда людей", light=30, heavy=20, druid=13)
    orcs_team = Army("Команда орков", berserk=20, shaman=15)

    # battle1 = Battle(humans_team=humans_team, orcs_team=orcs_team, index=1)
    # battle2 = Battle(humans_team=humans_team, orcs_team=orcs_team, index=2)
    # battle1.start()
    # battle2.start()

    battles = [Battle(humans_team=humans_team, orcs_team=orcs_team, index=i) for i in range(0, 100)]
    for battle in battles:
        battle.start()
