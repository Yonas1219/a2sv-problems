class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        N = len(nums)
        nums.sort()
        
        best = 0
        for index in range(N):
            best = max(best, nums[index] + nums[N - index -1])
        return best
