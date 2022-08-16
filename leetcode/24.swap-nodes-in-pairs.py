'''
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
'''
import Util


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # O(n) 40ms 91%
    def swapPairs(self, head: ListNode) -> ListNode:
        dummyHead = ListNode(None)
        dummyHead.next = head
        p = dummyHead
        while p.next is not None and p.next.next is not None:
            # 初始数据
            node1, node2 = p.next, p.next.next
            nextP = node2.next
            # 交换节点
            node2.next = node1
            node1.next = nextP
            p.next = node2
            # 后移指针
            p = node1
        return dummyHead.next


if __name__ == "__main__":
    head = Util.createList([1, 2, 3, 4])
    head = Solution().swapPairs(head)
    Util.printList(head)
