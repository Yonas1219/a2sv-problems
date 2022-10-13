from sortedcontainers import SortedList
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        sl = SortedList(x + 1 for x in range(n))
        
        current = len(sl) - 1
        while len(sl) - 1:
            current = (current + k) % len(sl)
            sl.remove(sl[current])
            current -= 1
        return sl[0]
