#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
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
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            # 是叶子节点 且 targetSum 被减道0了
            return targetSum == root.val
        return self.hasPathSum(root.left, targetSum - root.val) \
            or self.hasPathSum(root.right, targetSum - root.val)

# @lc code=end

