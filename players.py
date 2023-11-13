class Player:
    """A player has :
      a colour
      an attribute if it is his turn to play 
    """
    def __init__(self,
                 color):
        self._color = color

    @property
    def color(self):
        return self._color
    
class HumanPlayer(Player):
    """ A human player has one extra attribute, their name. 
    they will choose their move using the mouse"""
    def __init__(self,name,color):
        assert name.strip() != "", "invalid name"      
        super().__init__(color)
        self._name = name

    @property
    def name(self):
        return self._name
    

