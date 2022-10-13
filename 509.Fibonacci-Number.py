class Solution:
    def fib(self, N: int) -> int:
        seen = {0: 0, 1: 1}
        
        for i in range(2, N+1):
            seen[i] = seen[i-1] + seen[i-2]
            
        return (seen[N])
        
