class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        lookup = {")":"(","}":"{","]":"["}
        
        for p in s:
            if p in lookup.values():
                stack.append(p)
            elif stack and lookup[p] == stack[-1]:
                stack.pop()
            else:
                return False
        return stack == []
