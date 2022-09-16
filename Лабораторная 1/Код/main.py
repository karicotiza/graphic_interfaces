import dataclasses
import numpy as np
from PIL import Image


class Gamut:
    data_type = np.uint8


@dataclasses.dataclass
class Point:
    x: int
    y: int


@dataclasses.dataclass
class Colour(Gamut):
    value: int

    def __post_init__(self):
        if not (np.iinfo(super().data_type).min <= self.value <= np.iinfo(super().data_type).max):
            raise ValueError(
                f"Value must be between {np.iinfo(Gamut.data_type).min} and {np.iinfo(Gamut.data_type).max}"
            )
        self.value = super().data_type(self.value)

    def get_value(self):
        return self.value


class Board:
    def __init__(self, x: int, y: int, colour: Colour) -> None:
        self.__layer = np.full(
            shape=(x, y),
            fill_value=colour.get_value(),
            dtype=np.uint8,
        )

    def get_as_numpy_array(self) -> np.array:
        return self.__layer

    def draw_line(self, start_point: Point, end_point: Point, colour: Colour):
        self.__paint(start_point, colour)
        self.__paint(end_point, colour)

    def __paint(self, point: Point, colour: Colour) -> None:
        self.__layer[point.x][point.y] = colour.get_value()


if __name__ == "__main__":
    board = Board(50, 50, Colour(255))
    board.draw_line(
        Point(10, 10),
        Point(10, 25),
        Colour(0)
    )

    image = Image.fromarray(board.get_as_numpy_array())
    image.show(title="image")
    image.save("image.png")
