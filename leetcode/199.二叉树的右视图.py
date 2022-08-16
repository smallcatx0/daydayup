#
# @lc app=leetcode.cn id=199 lang=python3
#
# [199] 二叉树的右视图
#
from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
class Solution:
    # 97.15%(32 ms)  82.39%(14.8 MB)
    def rightSideView1(self, root: TreeNode) -> List[int]:
        # 层序遍历
        if root == None:
            return []
        res = []
        queue = [(0, root)]
        while len(queue) != 0:
            level, node = queue.pop()
            if len(res) == level:
                res.append([])
            res[level] = node.val
            if node.left != None:
                queue.insert(0, (level + 1, node.left))
            if node.right != None:
                queue.insert(0, (level + 1, node.right))
        return res

    # 
    def rightSideView(self, root: TreeNode) -> List[int]:
        # 层序遍历
        if root == None:
            return []
        res = []
        queue = [(0, root)]
        while len(queue) != 0:
            level, node = queue.pop()
            if len(res) == level:
                res.append([])
            res[level] = node.val
            if node.left != None:
                queue.insert(0, (level + 1, node.left))
            if node.right != None:
                queue.insert(0, (level + 1, node.right))
        return res
    
# @lc code=end

