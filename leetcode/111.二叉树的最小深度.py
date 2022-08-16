#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
class Solution:
    # 深度优先搜索遍历
    def minDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 1
        minDep = 10**9
        if root.left:
            minDep = min(minDep, self.minDepth(root.left))
        if root.right:
            minDep = min(minDep, self.minDepth(root.right))
        return minDep + 1
# @lc code=end
