#
# @lc app=leetcode.cn id=509 lang=python3
#
# [509] 斐波那契数
#

# @lc code=start
class Solution:
    _cacheMap = {0:0, 1:1, 2:1, 3:2, 4:3, 5:5, 6:8, 7:13, 8:21, 9:34, 10:55, 11:89, 12:144, 13:233, 14:377, 15:610, 16:987, 17:1597, 18:2584, 19:4181, 20:6765}
    def fib(self, N: int) -> int:
        if N in self._cacheMap.keys():
            return self._cacheMap[N]
        tasks ,res = [N, ], 0
        while len(tasks) > 0:
            t = tasks.pop()
            if t - 1 in self._cacheMap.keys() and t - 2 in self._cacheMap.keys():
                self._cacheMap[t] = self._cacheMap[t - 1] + self._cacheMap[t - 2]
                res += self._cacheMap[t]
                continue
            if t - 2 in self._cacheMap.keys():
                res += self._cacheMap[t - 2]
            else:
                tasks.append(t - 2)
            if t - 1 in self._cacheMap.keys():
                res += self._cacheMap[t - 1]
            else:
                tasks.append(t - 1)
        return res
# @lc code=end

if __name__ == "__main__":
    res = Solution().fib(30)
    print(res)