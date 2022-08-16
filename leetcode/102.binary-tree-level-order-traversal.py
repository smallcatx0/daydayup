'''
给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）
'''


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    # 数组模拟队列 60ms 36.38%
    def levelOrder(self, root):
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
        return res

    # 系统提供队列 60ms 36.38%
    def levelOrder2(self, root):
        res = []
        if root is None:
            return res
        from queue import Queue
        q = Queue()
        q.put((0, root))
        while not q.empty():
            level, node = q.get()
            if len(res) == level:
                res.append([])
            res[level].append(node.val)
            if node.left:
                q.put((level + 1, node.left))
            if node.right:
                q.put((level + 1, node.right))
        return res


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    res = Solution().levelOrder(root)
    print(res)
    res = Solution().levelOrder2(root)
    print(res)
