class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num <= 0: return False
        if num & num - 1 != 0: return False
        b = bin(num)[::-1]
        p = b.index("1")
        return p % 2 == 0
