#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层序遍历
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
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        queue = [(0, root)]
        res = []
        while len(queue) != 0:
            level, node = queue.pop()
            if(len(res) == level):
                res.append([])
            res[level].append(node.val)
            if node.left != None:
                queue.insert(0,(level + 1, node.left))
            if node.right != None:
                queue.insert(0,(level + 1, node.right))
        # 基数索引，反转
        for i in range(0, level + 1):
            if i % 2:
                res[i].reverse()
        return res

# @lc code=end


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    res = Solution().zigzagLevelOrder(root)
    print(res)