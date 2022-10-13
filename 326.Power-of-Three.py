class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        A = 3**19
        
        return n > 0 and A % n == 0
