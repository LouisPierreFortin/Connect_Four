from Status import *

class Diagonal:

    def __init__(self,
                 dicts : dict[tuple[int,int], Status],
                 lists : list[tuple[int, int]]):
        self._dict_status = dicts
        self._grid_list = lists

    def check_win(self, last_played: tuple[int, int]) -> bool:
        if self._right(last_played):
            return True
        elif self._left(last_played):
            return True
        else:
            return False

    def _right(self, last_played: tuple[int, int]) -> bool:
        pos_list = [last_played]
        steps = 1

        while True:
            if (last_played[0] - steps, last_played[1] - steps) in self._grid_list:
                pos_list.append((last_played[0] - steps, last_played[1] - steps))
                steps += 1
            else:
                steps = 1
                break

        while True:
            if (last_played[0] + steps, last_played[1] + steps) in self._grid_list:
                pos_list.append((last_played[0] + steps, last_played[1] + steps))
                steps += 1
            else:
                break

        p1 = 0
        p2 = 0
        for pos in pos_list:
            if self._dict_status.get(pos) == Status.P1:
                p1 += 1
                p2 = 0
            if self._dict_status.get(pos) == Status.P2:
                p2 += 1
                p1 = 0
            if p1 == 4:
                return True
            if p2 == 4:
                return True
        return False

    def _left(self, last_played: tuple[int, int]) -> bool:
        pos_list = [last_played]
        steps = 1

        while True:
            if (last_played[0] - steps, last_played[1] + steps) in self._grid_list:
                pos_list.append((last_played[0] - steps, last_played[1] + steps))
                steps += 1
            else:
                steps = 1
                break

        while True:
            if (last_played[0] + steps, last_played[1] - steps) in self._grid_list:
                pos_list.append((last_played[0] + steps, last_played[1] - steps))
                steps += 1
            else:
                break

        p1 = 0
        p2 = 0
        for pos in pos_list:
            if self._dict_status.get(pos) == Status.P1:
                p1 += 1
                p2 = 0
            if self._dict_status.get(pos) == Status.P2:
                p2 += 1
                p1 = 0
            if p1 == 4:
                return True
            if p2 == 4:
                return True
        return False