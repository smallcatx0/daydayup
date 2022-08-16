#
# @lc app=leetcode.cn id=107 lang=python3
#
# [107] 二叉树的层序遍历 II
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
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        res = []
        if root is None:
            return res
        queue = [(0, root)]
        while len(queue) != 0:
            level, node = queue.pop()
            if len(res) == level:
                res.append([])
            res[level].append(node.val)
            if node.left:
                queue = [(level + 1, node.left)] + queue
            if node.right:
                queue = [(level + 1, node.right)] + queue
        ret = []
        while len(res) != 0:
            ret.append(res.pop())
        return ret

# @lc code=end


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    res = Solution().levelOrderBottom(root)
    print(res)