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
            intensity: tp.Intensity
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
            colour,
            intensity
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
                intensity
            )

        return layer

    @staticmethod
    def bresenham(
            layer: bd.Layer,
            start_point: tp.Point,
            end_point: tp.Point,
            colour: tp.Colour,
            intensity: tp.Intensity
    ):
        delta_width = end_point.width - start_point.width
        delta_height = end_point.height - start_point.height

        sign_width = 1 if delta_width > 0 else -1 if delta_width < 0 else 0
        sign_height = 1 if delta_height > 0 else -1 if delta_height < 0 else 0

        if delta_width < 0:
            delta_width = -delta_width
        if delta_height < 0:
            delta_height = -delta_height

        if delta_width > delta_height:
            padding_delta_width, padding_delta_height = sign_width, 0
            es, el = delta_height, delta_width
        else:
            padding_delta_width, padding_delta_height = 0, sign_height
            es, el = delta_width, delta_height

        width, height = start_point.width, start_point.height

        error, index = el / 2, 0

        layer.paint(
            tp.Point(height, width),
            colour,
            intensity
        )

        while index < el:
            error -= es
            if error < 0:
                error += el
                width += sign_width
                height += sign_height
            else:
                width += padding_delta_width
                height += padding_delta_height
            index += 1
            layer.paint(
                tp.Point(height, width),
                colour,
                intensity,
            )

        return layer

    @staticmethod
    def wu(
            layer: bd.Layer,
            start_point: tp.Point,
            end_point: tp.Point,
            colour: tp.Colour,
            intensity: tp.Intensity
    ):

        return layer
