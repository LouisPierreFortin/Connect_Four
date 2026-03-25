from Grid import *

class Position:

    def __init__(self, pos : tuple[int,int]):
        self.pos = pos

    @property
    def pos(self):
        return self._pos

    @pos.setter
    def pos(self, value):
        if isinstance(value, tuple):
            if type(coords for coords in value) != int:
                if len(value) == 2:
                    if 0 <= value[0] <= Grid.gridx and 0 <= value[1] <= Grid.gridy:
                        self._pos = value
                    else:
                        raise ValueError("Dimension not in grid")
                else:
                    raise IndexError("Dimension must be written with only two coordinates")
            else:
                raise TypeError("Coords must be integers")
        else:
            raise TypeError("Dimension must be written as (x,y)")
if __name__ == "__main__":
    grid = Position((0,0))