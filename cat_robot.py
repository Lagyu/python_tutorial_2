from abc import ABCMeta, abstractmethod
import datetime


class AbstractTaste(metaclass=ABCMeta):
    def __init__(self, sweetness=0.0, sourness=0.0, saltiness=0.0, bitterness=0.0, savory=0.0):
        super().__init__()
        self.bitterness = bitterness
        self.saltiness = saltiness
        self.savory = savory
        self.sourness = sourness
        self.sweetness = sweetness

    def __repr__(self):
        return "<Taste object : (苦味: {0:.1f}, 塩味: {1:.1f}, うまみ: {2:.1f}, 酸味: {3:.1f}, 甘味: {4:.1f})>".format(self.bitterness, self.saltiness, self.savory, self.sourness, self.sweetness)

    @abstractmethod
    def get_values_list(self) -> list:
        return [self.bitterness, self.saltiness, self.savory, self.sourness, self.sweetness]

    @abstractmethod
    def get_subjective_value(self) -> float:
        return sum(self.get_values_list())


class Taste(AbstractTaste):
    def __init__(self, sweetness=0.0, sourness=0.0, saltiness=0.0, bitterness=0.0, savory=0.0):

        super().__init__(sweetness=sweetness, sourness=sourness, saltiness=saltiness, bitterness=bitterness, savory=savory)

    def get_values_list(self) -> list:
        return [self.bitterness, self.saltiness, self.savory, self.sourness, self.sweetness]

    def get_subjective_value(self) -> float:
        return sum(self.get_values_list())


class AbstractFood(metaclass=ABCMeta):
    def __init__(self, name: str, taste: Taste):
        self.name = name
        self.taste = taste

    def __repr__(self):
        return str([self.name, self.taste])


class Food(AbstractFood):
    pass


class CatRobot:
    def __init__(self, name: str, like: AbstractFood):

        self.name = name
        self.like = like

    def time_leap(self, to_datetime: datetime.datetime):
        print("Successful time leap to {0:%Y/%m/%d %H:%M:%S}".format(to_datetime))

    def ask_like(self):
        print("I like", self.like)


doraemon = CatRobot(name="どらえもん", like=Food(name="どらやき", taste=Taste(sweetness=100.0)))
doraemon.time_leap(datetime.datetime(2018, 3, 1, 12, 23, 15, 55))
doraemon.ask_like()




