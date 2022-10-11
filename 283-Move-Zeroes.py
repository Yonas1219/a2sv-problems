class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = 0
        for r in range(len(nums)):
            if nums[r]:
                nums[k], nums[r] = nums[r], nums[k]
                k += 1
        return nums
