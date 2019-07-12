import random
import math
from abc import ABCMeta, abstractmethod
from typing import List, TypeVar, Union


IntOrListOfInt = Union[int, List[int]]


class AbstractDice(metaclass=ABCMeta):
    def __init__(self, surfaces=6):
        self.surfaces = surfaces
        self.face = None

    @abstractmethod
    def roll(self, cycles=1) -> IntOrListOfInt:
        pass


class CubeDice(AbstractDice):
    def __init__(self):
        super().__init__()

    def roll(self, cycles=1) -> IntOrListOfInt:
        if cycles == 1:
            result = math.ceil(random.random() * 6)  # type: IntOrListOfInt
            self.face = result
            return result
        else:
            result = [math.ceil(random.random() * 6) for cycle in range(cycles)]
            self.face = result[-1]
            return result


class VersatileDice(AbstractDice):
    def __init__(self, surfaces=6):
        super().__init__(surfaces)

    def roll(self, cycles=1) -> IntOrListOfInt:
        if cycles == 1:
            result = math.ceil(random.random() * self.surfaces)  # type: IntOrListOfInt
            self.face = result
            return result
        else:
            result = [math.ceil(random.random() * self.surfaces) for cycle in range(cycles)]
            self.face = result[-1]
            return result


dice1 = CubeDice()
print(dice1.roll())
print(dice1.roll(10))
# print(dice1.face)


dice2 = VersatileDice(100)
print(dice2.roll())
print(dice2.roll(10))
# print(dice2.facmy




