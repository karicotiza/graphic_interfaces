from dataclasses import dataclass

import numpy as np


class Gamut:
    size = np.uint8


class Picture:
    size = np.uint16


def get_max(size: np.generic) -> int:
    return np.iinfo(size).max


def get_min(size: np.generic) -> int:
    return np.iinfo(size).min


def validate(*args: int, generic: np.generic) -> list:
    minimum = get_min(generic)
    maximum = get_max(generic)
    result = []
    for variable in args:
        if get_min(generic) <= variable <= get_max(generic):
            result.append(variable)
        else:
            raise ValueError(f"Value must be between {minimum} and {maximum}")
    return result


@dataclass
class Dimension:
    size: int

    def __post_init__(self):
        self.size = validate(
            self.size,
            generic=Picture.size
        )[0]


@dataclass
class Point:
    height: int
    width: int

    def __post_init__(self):
        self.height, self.width = validate(
            self.height,
            self.width,
            generic=Picture.size
        )


@dataclass
class Colour:
    red: int
    green: int
    blue: int

    def __post_init__(self):
        self.red, self.green, self.blue = validate(
            self.red,
            self.green,
            self.blue,
            generic=Gamut.size,
        )

    def get_rgb(self):
        return np.array([self.red, self.green, self.blue], dtype=Gamut.size)

    def get_grey(self):
        grey = np.mean(self.get_rgb())
        return np.array([grey in range(self.get_size())], dtype=Gamut.size)

    @staticmethod
    def get_size():
        return 3