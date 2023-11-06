class Square:
    def __init__(self,
                 state,
                 colorinside, 
                 coloroutline):
        self._state = self  
        self._colorinside = colorinside     #color of the square
        self._coloroutline = coloroutline   #color of the outline of the square

    @property
    def coloroutline(self):
        return self._coloroutline
    
    @property
    def colorinside(self):
        return self._colorinside
    
    @property
    def state(self):
        return self._state
    

class SmallSquare(Square):
    def __init__(self, state, colorinside, coloroutline):
        super().__init__(state, colorinside, coloroutline)
        


class BigSquare(Square):
    def __init__(self, state, colorinside, coloroutline):
        super().__init__(state, colorinside, coloroutline)

