class Raspberry:

    def __init__(self, index):
        self._states = iter(["Отсутствует", "Цветение", "Зеленая", "Красная"])
        self._index = index
        self._state = next(self._states)

    def grow(self):
        self._state = next(self._states)

    def is_ripe(self):
        return self._state == "Красная"


class RaspberryBush:

    def __init__(self, rasp_count):
        self.raspberries = [Raspberry(i) for i in range(rasp_count)]

    def grow_all(self):
        for rasp in self.raspberries:
            rasp.grow()

    def all_is_ripe(self):
        return all(map(Raspberry.is_ripe, self.raspberries))

    def give_away_all(self):
        self.raspberries.clear()


class Human:
    def __init__(self, name, plant):
        self.name = name
        self._plant: RaspberryBush = plant

    def work(self):
        self._plant.grow_all()

    def harvest(self):
        self._plant.give_away_all() if self._plant.all_is_ripe() else print("Ещё рано")

    @staticmethod
    def knowledge_base():
        print("Сажать во время парада планет, собирать когда рак на горе свистнет")


Human.knowledge_base()
bush = RaspberryBush(100)
human = Human("Denis, kotoriy ne smog", bush)
while not bush.all_is_ripe():
    human.work()
human.harvest()
