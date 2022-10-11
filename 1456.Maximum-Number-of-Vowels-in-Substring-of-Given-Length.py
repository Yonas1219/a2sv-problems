class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a','e','i','o','u'}
        vcount = 0
        
        for i in range(k):
            if s[i] in vowels: vcount += 1
        l = 0
        r = k - 1
        mvc = vcount
        while r < len(s)-1:
            if s[l] in vowels: vcount -= 1
            l += 1
            r += 1
            if s[r] in vowels: vcount += 1
            mvc = max(mvc, vcount)
        return mvc
                
