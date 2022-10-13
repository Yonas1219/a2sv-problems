class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        Mdd = 10 ** 9 + 7
        
        top = pow(2, p, Mdd) - 1
        mid = top - 1
        midcount = pow(2, p - 1, Mdd) - 1
        return (pow(mid, midcount, Mdd) * top) % Mdd
