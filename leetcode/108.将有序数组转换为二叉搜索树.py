#
# @lc app=leetcode.cn id=108 lang=python3
#
# [108] 将有序数组转换为二叉搜索树
#

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        l = len(nums)
        if l == 0:
            return None
        mid = l // 2
        node = TreeNode()
        node.val = nums[mid]
        node.left = self.sortedArrayToBST(nums[0: mid])
        node.right = self.sortedArrayToBST(nums[mid+1: l]) 
        return node
# @lc code=end


if __name__ == '__main__':
    res = Solution().sortedArrayToBST([1,2,3,4,5,6,7])
    print(res)