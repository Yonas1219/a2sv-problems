class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        def get_prefix_sum():
            
            prefix_sum = [0]*(L+1)
            for i in range(L):
                prefix_sum[i+1] = prefix_sum[i] + nums[i]
            return prefix_sum
        
        def dfs(i, N):
            
            if not N:
                return [], 0
            
            if L-i < k*N:
                return None, -float("inf")
            
            if (i, N) in memo:
                return memo[(i, N)]
            
            include, cnt_in = dfs(i+k, N-1) 
            include, cnt_in = [i] + include, cnt_in+prefix_sum[i+k]-prefix_sum[i] 
            
            exclude, cnt_ex = dfs(i+1, N) 
            if cnt_in >= cnt_ex: 
                memo[(i,N)] = include, cnt_in
                
            else:
                memo[(i,N)] = exclude, cnt_ex
            return memo[(i,N)]
        
        memo = {}
        L = len(nums)
        prefix_sum = get_prefix_sum()
        return dfs(0, 3)[0]
