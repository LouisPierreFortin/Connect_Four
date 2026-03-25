from typing import overload

from Status import *
from Position import *
from colorama import Fore, Back, init
init(autoreset=True)

class Grid:

    gridx = 7
    gridy = 6

    def __init__(self):

        self.grid = Grid._getgrid()
        """
        index of grid:
        
            0  1  2  3  4  5  6
        
        0   00 01 02 03 04 05 06 
        1   07 08 09 10 11 12 13 
        2   14 15 16 17 18 19 20 
        3   21 22 23 24 25 26 27 
        4   28 29 30 31 32 33 34 
        5   35 36 37 38 39 40 41 
        """
        self.dict_status = self._status()

    @classmethod
    def _getgrid(cls) -> list[tuple[int, int]]:

        grid : list[None|tuple[int,int]] = []
        for i in range(cls.gridy):
            for j in range(cls.gridx):
                grid.append((i,j))
        return grid


    @overload
    def _status(self, new : Status, *args):

        temp_dict : dict[tuple[int,int], Status] = {}
        for i in range(Grid.gridy * Grid.gridx):
            temp_dict[self.grid[i]] = Status.INACTIVE
        return temp_dict

    @overload
    def _status(self, new : Status, *args):
        pass

    def __str__(self):
        result : str = "   1  2  3  4  5  6  7\n"
        for i in range(6):
            result += f"{i + 1} "
            for j in range(7):
                result += f"{"[ ]"}"
            result += "\n"
        return result


if __name__ == '__main__':
    grid = Grid()
    print(grid)
    print(grid.dict_status)
