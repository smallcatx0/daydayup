'''
给定一个二叉树，返回它的 前序 遍历
'''
from typing import *


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 递归方式 32ms 99.19%
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        ret = [root.val]
        if root.left:
            ret += self.preorderTraversal(root.left)
        if root.right:
            ret += self.preorderTraversal(root.right)
        return ret

    # 递归方式32ms 99.19%
    def preorderTraversal1(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)

    # 非递归方式(迭代) 44ms 77.78%
    def preorderTraversal2(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        stack = [root]
        res = []
        while len(stack) != 0:
            cur = stack.pop()
            res.append(cur.val)
            if cur.right is not None:
                stack.append(cur.right)
            if cur.left is not None:
                stack.append(cur.left)
        return res


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    res1 = Solution().preorderTraversal(root)
    res2 = Solution().preorderTraversal1(root)
    print(res1)
    print(res2)
