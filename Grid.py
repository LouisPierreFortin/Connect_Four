class Grid:

    gridx = 7
    gridy = 6

    def __init__(self):

        self.grid = Grid._getgrid()

    @classmethod
    def _getgrid(cls):

        grid : list[None|tuple[int,int]] = []
        for i in range(cls.gridy):
            for j in range(cls.gridx):
                grid.append((i,j))
        return grid

    def __str__(self):
        result : str = ""
        for i in range(6):
            result += f"{"[ ]" *7}\n"
        return result

if __name__ == '__main__':
    grid = Grid()
    print(grid)
