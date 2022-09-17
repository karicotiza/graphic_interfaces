import canvas
from random import randint

if __name__ == "__main__":
    layer = canvas.Layer(
        height=canvas.Dimension(50),
        width=canvas.Dimension(50),
        colour=canvas.Colour(255, 255, 255)
    )

    for _ in range(500):
        layer = canvas.Brush.plus(
            layer,
            canvas.Point(
                randint(1, layer.height - 2),
                randint(1, layer.width - 2),
            ),
            canvas.Colour(
                randint(0, 255),
                randint(0, 255),
                randint(0, 255),
            )
        )

    layer.show()
    layer.save("image.png")
