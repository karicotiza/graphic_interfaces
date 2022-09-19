import layer as bd
import type as tp
import numpy as np


class Lines:
    @staticmethod
    def dda(
            layer: bd.Layer,
            start_point: tp.Point,
            end_point: tp.Point,
            colour: tp.Colour,
    ):
        length = max(
            abs(
                start_point.height - end_point.height
            ),
            abs(
                start_point.width - end_point.width
            )
        )

        d_width = (end_point.width - start_point.width) / length
        d_height = (end_point.height - start_point.height) / length

        layer.paint(
            start_point,
            colour
        )

        for _ in range(length):
            start_point.height += d_height
            start_point.width += d_width
            layer.paint(
                tp.Point(
                    int(np.round(start_point.height, 0)),
                    int(np.round(start_point.width, 0)),
                ),
                colour,
            )

        return layer
