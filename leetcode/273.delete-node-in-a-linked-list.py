'''
请编写一个函数，使其可以删除某个链表中给定的（非末尾）节点，你将只被给定要求被删除的节点。
'''
import Util


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # O(1) 48ms 91.33%
    def deleteNode(self, node):
        if node is None:
            return
        delNode = node.next
        if delNode is None:
            del node
            node = None
        else:
            node.val = delNode.val
            node.next = delNode.next
            del delNode
        return


if __name__ == "__main__":
    head = Util.createList([1, 2, 3])
    delNode = head.next.next
    Solution().deleteNode(delNode)
    Util.printList(head)
