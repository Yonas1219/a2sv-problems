class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        N = len(nums)
        h = [(-nums[0],0)]
        
        for i in range(1,N):
            while h[0][1]<i-k:
                heappop(h)
            max_so_far = h[0][0]
            heappush(h,(max_so_far-nums[i],i))
            if i == N-1:
                return -(max_so_far-nums[i])
        return nums[0]
                
