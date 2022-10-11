class MinStack:

    def __init__(self):
        self.s1 = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.s1.append(val)
        
        if not self.min_stack or val < self.min_stack[-1][0]:
            self.min_stack.append([val,1])
        elif self.min_stack[-1][0] == val:
            self.min_stack[-1][1] += 1
        

    def pop(self) -> None:
        if self.min_stack[-1][0] == self.s1[-1]:
            self.min_stack[-1][1] -= 1
        if self.min_stack[-1][1] == 0:
            self.min_stack.pop()
        self.s1.pop()
    def top(self) -> int:
        return self.s1[-1]

    def getMin(self) -> int:
        return self.min_stack[-1][0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
