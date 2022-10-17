class Solution:
    def countVowels(self, word: str) -> int:
        N = len(word)
        count = 0
        
        for i, x in enumerate(word):
            if x in "aeiou":
                count += (i + 1) * ( N- i)
        return count
