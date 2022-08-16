#
# @lc app=leetcode.cn id=412 lang=python3
#
# [412] Fizz Buzz
#
from typing import List


# @lc code=start
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ret = []
        for i in range(1, n+1):
            if (i % 15) == 0:
                ret.append('FizzBuzz')
            elif (i % 5) == 0:
                ret.append('Buzz')
            elif (i % 3) == 0:
                ret.append('Fizz')
            else:
                ret.append(str(i))
        return ret
# @lc code=end

if __name__ == '__main__':
    n = 98
    res = Solution().fizzBuzz(n)
    print(res)