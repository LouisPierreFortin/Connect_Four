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
        self.dict_status = self.status()

    @classmethod
    def _getgrid(cls) -> list[tuple[int, int]]:

        grid : list[None|tuple[int,int]] = []
        for i in range(cls.gridy):
            for j in range(cls.gridx):
                grid.append((j,i))
        return grid

    @overload
    def status(self) -> dict[tuple[int,int], Status]: ...
    @overload
    def status(self, column : int, player = Status.P1) -> None: ...
    @overload
    def status(self, column : int, player = Status.P2) -> None: ...
    def status(self, *args, **kwargs) -> dict[tuple[int,int], Status] | None:

        if not kwargs and not args:
            temp_dict : dict[tuple[int,int], Status] = {}
            for i in range(Grid.gridy * Grid.gridx):
                temp_dict[self.grid[i]] = Status.INACTIVE
            return temp_dict
        elif kwargs["player"] == Status.P1:
            col = args[0]
            for key in self.dict_status:
                if key[1] == col:
                    if self.dict_status[key] != Status.INACTIVE:
                        raise ValueError("Full column")
                    else:
                        for l in range(Grid.gridy - 1):
                            print(l)
                            if self.dict_status[tuple([col, l + 1])] == Status.INACTIVE:
                                continue
                            else:
                                self.dict_status[tuple([col , l + 1])] = Status.P1
                                return None
                        else:
                            self.dict_status[tuple([col, l])] = Status.P1
                            return None
            return None
        else:
            return [args,kwargs]

    def status_update(self):
        pass

    def __str__(self):
        result : str = "   0  1  2  3  4  5  6\n"
        for i in range(6):
            result += f"{i} "
            for j in range(7):
                key = tuple([i,j])
                if self.dict_status[key] == Status.INACTIVE:
                    result += f"{Fore.RESET}[ ]"
                elif self.dict_status[key] == Status.P1:
                    result += f"{Fore.YELLOW}[ ]"
            result += f"\n"
        return result


if __name__ == '__main__':
    grid = Grid()
    #print(grid)
    print(grid.dict_status)
    grid.status(4, player = Status.P1)
    print(grid.dict_status)
    grid.status(4, player=Status.P1)
    print(grid.dict_status)
    print(grid)
