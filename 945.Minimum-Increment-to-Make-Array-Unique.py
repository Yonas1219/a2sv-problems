class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        if (A == None):
            return 0
        result = 0
        temp = 0
        A.sort()
        pre = A[0]
        for i in range(1,len(A)):
            temp = pre + 1
            result += max(temp - A[i], 0)
            pre = max(temp, A[i])
        return result
