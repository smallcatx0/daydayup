#
# @lc app=leetcode.cn id=232 lang=python3
#
# [232] 用栈实现队列
#

# @lc code=start
from typing import Deque
class MyQueue:
    # 98.88 %(28 ms)  93.08 %(14.8 MB)
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s = Deque()

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        l = []
        while len(self.s):
            l.append(self.s.pop())
        self.s.append(x)
        for i in range(len(l) - 1, -1, -1) :
            self.s.append(l[i])

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.s.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.s[-1]


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.s) == 0


# Your MyQueue object will be instantiated and called as such:
# @lc code=end
if __name__ == '__main__':
    obj = MyQueue()
    print(obj.push(1), sep=' ')
    print(obj.push(2), sep=' ')
    print(obj.push(3), sep=' ')
    print(obj.push(4), sep=' ')
    print(obj.pop(), sep=' ')
    print(obj.push(5), sep=' ')
    print(obj.pop(), sep=' ')
    print(obj.pop(), sep=' ')
    # print(obj.push(3))