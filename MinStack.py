# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/529/week-2/3292/
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_stack = []
        
    def push(self, x: int) -> None:
        new_min = min(x, self.getMin()) if self.min_stack else x
        self.min_stack.append((x, new_min))

    def pop(self) -> None:
        return self.min_stack.pop()[0]

    def top(self) -> int:
        return self.min_stack[-1][0]
        
    def getMin(self) -> int:
        return self.min_stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
