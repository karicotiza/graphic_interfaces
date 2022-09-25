import canvas

if __name__ == "__main__":
    layer = canvas.Layer(
        height=canvas.Dimension(50),
        width=canvas.Dimension(50),
        colour=canvas.Colour(255, 255, 255)
    )

    layer = canvas.Lines.wu(
        layer,
        canvas.Point(25, 10),
        canvas.Point(15, 40),
        canvas.Colour(255, 0, 0),
        canvas.Intensity(128)
    )

    layer = canvas.Lines.wu(
        layer,
        canvas.Point(10, 25),
        canvas.Point(40, 35),
        canvas.Colour(255, 255, 0),
        canvas.Intensity(128)
    )

    layer = canvas.Lines.wu(
        layer,
        canvas.Point(25, 40),
        canvas.Point(35, 10),
        canvas.Colour(0, 255, 255),
        canvas.Intensity(128)
    )

    layer = canvas.Lines.wu(
        layer,
        canvas.Point(40, 25),
        canvas.Point(10, 15),
        canvas.Colour(0, 0, 255),
        canvas.Intensity(128)
    )

    layer.show()
    layer.save("image.png")
