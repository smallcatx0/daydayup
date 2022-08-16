'''
给定一个二叉树，返回它的中序 遍历
'''
from typing import *


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 递归方式 32ms 99.7%
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        ret = []
        if root.left:
            ret += self.inorderTraversal(root.left)
        ret += [root.val]
        if root.right:
            ret += self.inorderTraversal(root.right)
        return ret

    # 递归方式 40ms 90%
    def inorderTraversal1(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        return self.inorderTraversal1(root.left) + [root.val] + self.inorderTraversal1(root.right)

    # 非递归方式 44ms 77.95%
    def inorderTraversal2(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        stack = [('go', root)]
        ret = []
        while len(stack) != 0:
            command = stack.pop()
            if command[0] == 'print':
                ret.append(command[1].val)
            else:
                if command[1].right:
                    stack.append(('go', command[1].right))
                stack.append(('print', command[1]))
                if command[1].left:
                    stack.append(('go', command[1].left))
        return ret


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    res = Solution().inorderTraversal(root)
    print(res)
    res = Solution().inorderTraversal1(root)
    print(res)
    res = Solution().inorderTraversal2(root)
    print(res)

