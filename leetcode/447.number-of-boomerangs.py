
'''
给定平面上 n 对不同的点，“回旋镖” 是由点表示的元组 (i, j, k) ，其中 i 和 j 之间的距离和 i 和 k 之间的距离相等（需要考虑元组的顺序）。找到所有回旋镖的数量。你可以假设 n 最大为 500，所有点的坐标在闭区间 [-10000, 10000] 中。

链接：https://leetcode-cn.com/problems/number-of-boomerangs
'''
from typing import *


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        ret = 0
        for i in range(len(points)):
            pMap = {}
            for j in range(len(points)):
                if i == j:
                    continue
                dis = (points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2
                if dis not in pMap:
                    pMap[dis] = 1
                else:
                    pMap[dis] += 1
            # print(pMap)
            for a in pMap:
                if pMap[a] >= 2:
                    ret += pMap[a] * (pMap[a] - 1)
        return ret


if __name__ == "__main__":
    points = [[0, 0], [1, 0], [2, 0]]
    points = [[0, 0], [1, 0], [-1, 0], [0, 1], [0, -1]]
    res = Solution().numberOfBoomerangs(points)
    # res = (points[0][0] - points[1][0])**2 + (points[0][1]-points[1][1])**2
    print(res)
