class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sumdict = {0:1}
        n = len(nums)
        count = 0
        s = 0
        
        for num in nums:
            s += num
            if s-k in sumdict:
                count += sumdict[s-k]
            if s in sumdict:
                sumdict[s] += 1
            else:
                sumdict[s] = 1
        return count
            