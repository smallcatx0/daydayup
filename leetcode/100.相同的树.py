#
# @lc app=leetcode.cn id=100 lang=python3
#
# [100] 相同的树
#

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # 两个树前序遍历
        return self.traverse(p, q)
    
    def traverse(self, p : TreeNode, q: TreeNode):
        if (p == None and q == None):
            return True
        if (p == None or q == None):
            return False
        if (p.val != q.val):
            # 全局推出
            return False
        if (not self.traverse(p.left, q.left)):
            return False
        if (not self.traverse(p.right, q.right)):
            return False
        return True
# @lc code=end

