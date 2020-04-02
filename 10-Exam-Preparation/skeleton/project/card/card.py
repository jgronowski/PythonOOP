from abc import ABC, abstractmethod

class Card(ABC):

    def __init__(self, name: str):
        self.name = name
        self.damage_points = 0
        self.health_points = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Card's name cannot be an empty string.")
        else:
            self.__name = value

    @property
    def damage_points(self):
        return self.__damage_points

    @damage_points.setter
    def damage_points(self, value):
        if value < 0:
            raise ValueError("Card's damage points cannot be less than zero.")
        self.__damage_points = value

    @property
    def health_points(self):
        return self.__health_points

    @health_points.setter
    def health_points(self, value):
        if value < 0:
            raise ValueError("Card's HP cannot be less than zero.")
        self.__health_points = value
