from Status import *

class Horizontal:

    def __init__(self,
                 dicts : dict[tuple[int,int], Status]):
        self._dict_status = dicts

    def check_win(self, last_played : tuple[int,int]) -> bool:
        line = last_played[1]
        p1 = 0
        p2 = 0
        for i in range(7):
            if self._dict_status.get((i, line)) == Status.P1:
                p1 += 1
                p2 = 0
            if self._dict_status.get((i, line)) == Status.P2:
                p2 += 1
                p1 = 0
            if p1 == 4:
                return True
            if p2 == 4:
                return True
        return False