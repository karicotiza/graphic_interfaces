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

    def paint(self, point: tp.Point, colour: tp.Colour, intensity: tp.Intensity) -> None:
        memory = []
        for index in range(colour.get_size()):
            memory.append(
                max(
                    int(colour.get_rgb()[index]),
                    int(self.__layer[point.height][point.width][index]) - int(intensity.value)
                )
            )

        self.__layer[point.height][point.width] = memory

    def show(self) -> None:
        Image.fromarray(self.__get_as_numpy_array()).show()

    def save(self, path: str) -> None:
        Image.fromarray(self.__get_as_numpy_array()).save(path)
