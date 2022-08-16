#
# @lc app=leetcode.cn id=225 lang=python3
#
# [225] 用队列实现栈
#


# @lc code=start
from queue import Queue
class MyStack:
    # 60.75 %(40 ms) 71.31 %(14.9 MB)
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = Queue()


    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q.put(x)
        l = self.q.qsize()
        while l > 1:
            self.q.put(self.q.get())
            l -= 1

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.q.get()

    def top(self) -> int:
        """
        Get the top element.
        """
        top = self.q.get()
        self.q.put(top)
        l = self.q.qsize()
        while l > 1:
            self.q.put(self.q.get())
            l -= 1
        return top


    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.q.empty()



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end


if __name__ == '__main__':
    st = MyStack()
    st.push(1)
    st.push(2)
    st.push(3)
    print(st.top())
    print(st.pop())
    print(st.pop())
    print(st.pop())