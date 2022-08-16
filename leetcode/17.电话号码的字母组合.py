#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#
from typing import List
import queue

# @lc code=start
class Solution:
    res = []
    digits = ""
    keyMap = [
        [], # 0
        [], # 1
        ['a','b','c'], # 2
        ['d','e','f'],
        ['g','h','i'],
        ['j','k','l'],
        ['m','n','o'],
        ['p','q','r','s'],
        ['t','u','v'],
        ['w','x','y','z'] # 9
    ]
    # 递归思路
    def letterCombinations1(self, digits: str) -> List[str]:
        self.digits = digits
        if digits != '':
            self.deep(0, '')
        return self.res
    
    def deep(self, index, tmpstr):
        tmpstrs = []
        for aChar in self.keyMap[int(self.digits[index])]:
            tmpstrs.append(tmpstr + aChar)
        # 递归到底
        if index == len(self.digits) - 1: 
            self.res = self.res + tmpstrs
        else:
            for one in tmpstrs:
                self.deep(index + 1, one)
    # 队列思路
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '':
            return []
        qus = queue.Queue()
        qus.put('')
        for one in digits:
            # 出队次数
            outNum = qus.qsize()
            while outNum > 0:
                outNum -= 1
                outStr = qus.get()
                for aChar in self.keyMap[int(one)]:
                    qus.put(outStr + aChar)
        res = []
        while qus.qsize() > 0:
            res.append(qus.get())
        return res

# @lc code=end
if __name__ == "__main__":
    res = Solution().letterCombinations("22")
    print(res)