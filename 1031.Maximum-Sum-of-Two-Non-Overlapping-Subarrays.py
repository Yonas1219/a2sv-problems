class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        def maxSum(A, L, M):
            ans = 0
            maxL = 0
            sumL = 0
            sumM = 0
            for i in range(len(A)):
                if (i < L or i >= L + M):
                    if i < L:
                         sumL += A[i]
                    else:
                        sumL += A[i - M]
                if (i >= L):
                    sumM += A[i]
                if (i >= L + M):
                    sumL -= A[i - L - M]
                if (i >= L + M):
                    sumM -= A[i - M]
                if (i >= L + M - 1): 
                    maxL = max(maxL, sumL)
                if (i >= L + M - 1):
                    ans = max(ans, maxL + sumM)
            return ans;
        return max(maxSum(A, L, M), maxSum(A, M, L))
