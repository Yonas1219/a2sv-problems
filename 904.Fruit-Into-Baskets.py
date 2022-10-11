class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        counter = defaultdict(int)
        
        left = 0
        ans = 0
        
        for right, f in enumerate(fruits):
            counter[f] += 1
            
            while len(counter) > 2:
                counter[fruits[left]] -= 1
                if counter[fruits[left]] == 0:
                    del counter[fruits[left]]
                left += 1
            ans = max(ans, right-left + 1)
        return ans
                    
                
        
