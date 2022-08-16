#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#
from typing import List

# @lc code=start
class Solution:
    def area(self, i, j, h):
        return min(h[i], h[j]) * (j - i)

    def maxArea1(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        maxArea = self.area(i, j, height)
        while i < j:
            area = self.area(i, j, height)
            if maxArea < area:
                maxArea = area
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return maxArea

    def maxArea(self, height: List[int]) -> int:
        area = -1
        i, j = 0, len(height) - 1
        while i < j:
            area = max(area, min(height[i], height[j]) * (j - i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return area

# @lc code=end


if __name__ == "__main__":
    heigths = [1, 8, 6, 2, 13, 4, 8, 19, 7]
    heigths = [2, 3, 4, 5, 18, 17, 6]
    heigths = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    res = Solution().maxArea1(heigths)
    # res = Solution().area(0, 8, heigths)
    print(res)
