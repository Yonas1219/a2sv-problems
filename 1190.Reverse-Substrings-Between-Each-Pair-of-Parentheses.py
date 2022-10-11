class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack=[]
        string=''
        ans = None
        
        for char in s:
            if char.isalpha():
                string+=char
            elif char == '(':
                if string != None:
                    stack.append(string)
                    string = ''
                stack.append(char)
            else:
                while stack != None and stack[-1] != '(':
                    string = stack.pop() + string
                if stack and stack[-1] == '(':
                    stack.pop()
                    stack.append(string[::-1])
                    string = ''
        if string:
            stack.append(string)
        ans = ''.join(stack)
        return ans
                    
