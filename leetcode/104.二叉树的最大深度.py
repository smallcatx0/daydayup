#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
class Solution:
    # 56.22%(52 ms) 99.14%(15.6 MB)
    def maxDepth(self, root: TreeNode) -> int:
        # 层序遍历 返回层数
        if root == None:
            return 0
        level = 1
        queue = [(level, root)]
        while len(queue) != 0:
            level, node = queue.pop()
            if node.left != None:
                queue.insert(0,(level + 1, node.left))
            if node.right != None:
                queue.insert(0,(level + 1, node.right))
        return level
# @lc code=end

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    res = Solution().maxDepth(root)
    print(res)