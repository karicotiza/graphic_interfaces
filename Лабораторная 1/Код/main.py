import canvas

if __name__ == "__main__":
    layer = canvas.Layer(
        height=canvas.Dimension(50),
        width=canvas.Dimension(50),
        colour=canvas.Colour(255, 255, 255)
    )

    # layer = canvas.Lines.dda(
    #     layer,
    #     canvas.Point(10, 10),
    #     canvas.Point(20, 40),
    #     canvas.Colour(0, 255, 0)
    # )
    #
    layer = canvas.Lines.bresenham(
        layer,
        canvas.Point(10, 10),
        canvas.Point(40, 40),
        canvas.Colour(255, 0, 0),
        canvas.Intensity(255)
    )

    layer = canvas.Lines.bresenham(
        layer,
        canvas.Point(10, 20),
        canvas.Point(40, 35),
        canvas.Colour(0, 255, 0),
        canvas.Intensity(128)
    )

    layer = canvas.Lines.bresenham(
        layer,
        canvas.Point(10, 25),
        canvas.Point(40, 30),
        canvas.Colour(0, 0, 255),
        canvas.Intensity(64)
    )

    # layer = canvas.Lines.wu(
    #     layer,
    #     canvas.Point(0, 0),
    #     canvas.Point(49, 10),
    #     canvas.Colour(255, 0, 0),
    #     canvas.Intensity(255)
    # )

    layer.show()
    layer.save("image.png")
