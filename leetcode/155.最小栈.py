#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] 最小栈
#
import math

# @lc code=start
class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        # 最小栈
        self.minStack = [math.inf]

    def push(self, x: int) -> None:
        self.data.append(x)
        # 维护最小栈
        currMix = self.getMin()
        if x < currMix:
            currMix = x
        self.minStack.append(currMix)

    def pop(self) -> None:
        self.data.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.data[len(self.data) - 1]

    def getMin(self) -> int:
        return self.minStack[len(self.minStack) - 1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

