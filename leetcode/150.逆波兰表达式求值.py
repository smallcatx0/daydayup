#
# @lc app=leetcode.cn id=150 lang=python3
#
# [150] 逆波兰表达式求值
#
from typing import List


# @lc code=start
class Solution:
    # O(n) 140ms
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        operSet = set(('+', '-', '*', '/'))
        for one in tokens:
            if one in operSet:
                num2 = st.pop()
                num1 = st.pop()
                # evalStr = "int(%s %s %s)" % (num1, one, num2)
                # res = eval(evalStr)
                # print(evalStr, '=', res)
                st.append(eval("int(%s %s %s)" % (num1, one, num2)))
            else:
                st.append(one)
        return st.pop()

# @lc code=end


if __name__ == "__main__":
    tokens = ["4", "13", "5", "/", "+"]
    res = Solution().evalRPN(tokens)
    print(res)
