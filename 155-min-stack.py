class MinStack:
    def __init__(self):
        self.minIndexes = []
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minIndexes) == 0 or val < self.stack[self.minIndexes[-1]]:
            self.minIndexes.append(len(self.stack) - 1)

    def pop(self) -> None:
        if len(self.stack) - 1 == self.minIndexes[-1]:
            self.minIndexes.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack[self.minIndexes[-1]]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
