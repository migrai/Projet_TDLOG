class Square:
    def __init__(self, state, color_inside, color_outline):
        self._state = self
        self._color_inside = color_inside  # color of the square
        self._color_outline = color_outline  # color of the outline of the square

    @property
    def color_outline(self):
        return self._color_outline

    @property
    def color_inside(self):
        return self._color_inside

    @property
    def state(self):
        return self._state


class SmallSquare(Square):
    def __init__(self, state, color_inside, color_outline):
        super().__init__(state, color_inside, color_outline)


class BigSquare(Square):
    def __init__(self, state, color_inside, color_outline):
        super().__init__(state, color_inside, color_outline)
