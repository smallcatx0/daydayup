#
# @lc app=leetcode.cn id=404 lang=python3
#
# [404] 左叶子之和
#

# Definition for a binary tree node.
from _typeshed import Self


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
class Solution:
    def isLeaf(self, root: TreeNode) -> bool:
        return root and not root.left and not root.right
    # 87.87%(32ms) 66.69%(15.4MB)
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        sum = 0
        if root == None:
            return 0
        if self.isLeaf(root.left):
            sum = root.left.val
        else:
            sum += self.sumOfLeftLeaves(root.left)
        return sum + self.sumOfLeftLeaves(root.right)
# @lc code=end

