from random import random as r


class Player:
    def __init__(self, name):
        self.name = name
        self.dodge_chance = 0.8
        self.points = 0

    def hit(self):
        if r() < self.dodge_chance:
            return True
        else:
            return False


class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.points1 = 0
        self.points2 = 0
        self.train_points1 = 0
        self.train_points2 = 0
        self.first_pl = None
        self.second_pl = None

    def start_game(self):
        while self.train_points1 < 1 and self.train_points2 < 1:
            if not self.player1.hit():
                self.train_points2 += 1
            if not self.player2.hit():
                self.train_points1 += 1
        self.first_pl = self.player1 if self.train_points1 == 1 else self.player2
        self.second_pl = self.player2 if self.train_points2 == 1 else self.player1

        while self.first_pl.points < 11 and self.second_pl.points < 11:
            if not self.first_pl.points == 10 and self.second_pl.points == 10:
                self.first_pl.dodge_chance += 0.05
                self.second_pl.dodge_chance -= 0.05
                flag = False
                for i in range(3):
                    if not self.first_pl.hit():
                        self.second_pl.points += 1
                        flag = True
                    elif not self.second_pl.hit():
                        self.first_pl.points += 1
                        flag = True
                    if flag:
                        break
                self.first_pl.dodge_chance -= 0.05
                self.second_pl.dodge_chance += 0.05
                self.first_pl, self.second_pl = self.second_pl, self.first_pl
            else:
                self.first_pl.dodge_chance += 0.05
                self.second_pl.dodge_chance -= 0.05
                if not self.first_pl.hit():
                    self.second_pl.points += 1
                elif not self.second_pl.hit():
                    self.first_pl.points += 1

                self.first_pl.dodge_chance -= 0.05
                self.second_pl.dodge_chance += 0.05
                self.first_pl, self.second_pl = self.second_pl, self.first_pl
        return f"winner: {self.first_pl.name if self.first_pl.points == 11 else self.second_pl.name}"


p1, p2 = Player("Ping"), Player("Pong")
game = Game(p1, p2)
print(game.start_game())
