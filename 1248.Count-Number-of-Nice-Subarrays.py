class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def f(k): # number of substring with at most k odd numbers
            res = i = j = countOdd = 0
            while j < len(nums):
                countOdd += nums[j] % 2
                while countOdd > k: # to shrink the window
                    countOdd -= nums[i] % 2
                    i += 1
                res += j - i + 1
                j += 1
            return res
        return f(k) - f(k-1)