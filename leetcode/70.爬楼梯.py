#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        retMap = { 1:1, 2:2, 3:3 }
        if n in retMap.keys():
            return retMap[n]
        tasks, ret = [n,], 0
        # addtime = 0
        while len(tasks) != 0:
            t = tasks.pop()
            # 计算缓存
            if t-1 in retMap.keys() and t-2 in retMap.keys():
                retMap[t] = retMap[t - 1] + retMap [t - 2]
                ret += retMap[t]
                # addtime += 1
                continue
            if t-1 not in retMap.keys():
                tasks.append(t-1)
            else:
                ret += retMap[t - 1]
                # addtime += 1
            if t-2 not in retMap.keys():
                tasks.append(t - 2)
            else:
                ret += retMap[t - 2]
                # addtime += 1
        return ret
        
# @lc code=end

if __name__ == "__main__":
    res = Solution().climbStairs(9)
    print(res)