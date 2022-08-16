#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        return self.f(root.left, root.right)

    def f(self, l : TreeNode, r: TreeNode) -> bool:
        if l == None and r == None:
            return True
        if l == None or r == None:
            return False
        if l.val != r.val:
            return False
        if not self.f(l.left, r.right):
            return False
        if not self.f(l.right, r.left):
            return False
        return True
# @lc code=end

