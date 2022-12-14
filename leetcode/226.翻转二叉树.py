#
# @lc app=leetcode.cn id=226 lang=python3
#
# [226] 翻转二叉树
#

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
# Definition for a binary tree node.
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root == None:
            return
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
# @lc code=end
