class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        N = len(nums)
        
        has_cache = [[False] * (N + 1) for _ in range(N + 1)]
        cache = [[None] * (N + 1) for _ in range(N + 1)]
        
        def score(left, right):
            if left > right:
                return 0
            
            if has_cache[left][right]:
                return cache[left][right]
            
            score_taking_left = nums[left] - score(left + 1, right)
            score_taking_right = nums[right] - score(left, right - 1)
            
            has_cache[left][right] = True
            cache[left][right] = max(score_taking_left, score_taking_right)
            return cache[left][right]
        
        return score(0, N - 1) >= 0
            
