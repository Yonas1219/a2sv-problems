class Solution:
    def calculate(self, s: str) -> int:
        if len(s)==0:
            return 0
        ans = 0
        prev = 0
        curr = 0
        operator = '+'
        
        for i, c in enumerate(s):
            if c.isdigit():
                curr = curr * 10 + int(c)
            if not c.isdigit() and c != ' ' or i == len(s) - 1:
                if operator == '+' or operator == '-':
                    ans += prev
                    prev = (curr if operator == '+' else -curr)
                elif operator == '*':
                    prev *= curr
                elif operator == '/':
                     prev = int(prev / curr)
                operator = c
                curr = 0
                
        return ans + prev
