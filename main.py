from Grid import Grid
from Status import Status
from Position import Position

def _player_1(col : int) -> bool:
    pos = grid.status(col, player=Status.P1)
    if grid.check_win(pos):
        print("Player 1 wins!")

def _player_2(col : int) -> bool:
    pos = grid.status(col, player=Status.P2)
    if grid.check_win(pos):
        print("Player 2 wins!")

def main():
    global grid
    grid = Grid()
    while True:
        print(grid)
        _player_1(int(input("Where do you want to play (0-6)? ")))
        print(grid)
        _player_2(int(input("Where do you want to play (0-6)? ")))


if __name__ == "__main__":
    main()