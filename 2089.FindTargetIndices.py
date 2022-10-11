class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        ans = []
        
        for i, x in enumerate(nums):
            if x == target:
                ans.append(i)
        return ans
