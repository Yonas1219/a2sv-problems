class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        N = len(nums)
        
        def good(left, right):
            k = list(sorted(nums[left:right+1]))
            if len(k) == 1:
                return True
            delta = k[1] - k[0]
            for x, y in zip(k, k[1:]):
                if y - x != delta:
                    return False
            return True
        res = []
        for left, right in zip(l, r):
            res += [good(left, right)]
        return res
           
        
    
