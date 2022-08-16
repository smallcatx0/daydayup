'''
给定一个二叉树，返回它的 后序 遍历
'''
from typing import *


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 递归方式 44ms 78.56%
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]

    # 非递归方式 44ms 78.56%
    def postorderTraversal1(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        stack = [('go', root)]
        ret = []
        while len(stack) != 0:
            command = stack.pop()
            if command[0] == 'print':
                ret.append(command[1].val)
            else:
                stack.append(('print', command[1]))
                if command[1].right:
                    stack.append(('go', command[1].right))
                if command[1].left:
                    stack.append(('go', command[1].left))
        return ret


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    res = Solution().postorderTraversal(root)
    print(res)
    res = Solution().postorderTraversal1(root)
    print(res)
