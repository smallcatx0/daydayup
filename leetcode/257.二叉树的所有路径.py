#
# @lc app=leetcode.cn id=257 lang=python3
#
# [257] 二叉树的所有路径
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
    # 深度优先搜索遍历
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        ret = []
        def btpaths(root: TreeNode, paths: str):
            if not root:
                return None
            paths += str(root.val)
            if root.left == None and root.right == None:
                # 递归到底了
                ret.append(paths)
            else:
                paths += '->'
                btpaths(root.left, paths)
                btpaths(root.right, paths)
        btpaths(root, '')
        return ret

    
# @lc code=end
