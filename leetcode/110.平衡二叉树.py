#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
class Solution:
    def height(self, root: TreeNode) -> int:
        if root == None:
            return 0
        return max(self.height(root.left), self.height(root.right)) + 1

    def isBalanced(self, root: TreeNode) -> bool:
        if root == None:
            return True
        return abs(self.height(root.left)- self.height(root.right)) <= 1 and \
            self.isBalanced(root.left) and \
            self.isBalanced(root.right)
# @lc code=end

