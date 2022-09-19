import numpy as np
from PIL import Image

import type as tp


class Layer:
    def __init__(self, height: tp.Dimension, width: tp.Dimension, colour: tp.Colour) -> None:
        self.height = height.size
        self.width = width.size
        self.__layer = np.full(
            shape=(self.height, self.width, colour.get_size()),
            fill_value=colour.get_rgb(),
            dtype=tp.Gamut.size,
        )

    def __get_as_numpy_array(self) -> np.array:
        return self.__layer

    def paint(self, point: tp.Point, colour: tp.Colour) -> None:
        self.__layer[point.height][point.width] = colour.get_rgb()

    def show(self) -> None:
        Image.fromarray(self.__get_as_numpy_array()).show()

    def save(self, path: str) -> None:
        Image.fromarray(self.__get_as_numpy_array()).save(path)
