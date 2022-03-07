class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack or val <= self.minStack[-1]: self.minStack.append(val)
    
    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.minStack[-1]: self.minStack.pop()

    def top(self) -> int:
        val = self.stack[-1]
        return val

    def getMin(self) -> int:
        val = self.minStack[-1]
        print(self.minStack)
        return val
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()