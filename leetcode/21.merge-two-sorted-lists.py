'''
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的
'''
import Util


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    # O(n+m) 48 ms 87.12%
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummyHead = ListNode(None)
        dummyHead.next = l2
        p1, pre, p2 = l1, dummyHead, dummyHead.next
        while p1 is not None and p2 is not None:
            # 如果p1的值在pre与p2之间 则插入此节点到pre与p2之间
            if (pre.val is None or pre.val <= p1.val) and p1.val <= p2.val:
                moveNode = p1
                p1 = p1.next
                pre.next = moveNode
                moveNode.next = p2
                pre = moveNode
            else:  # 否则，移动pre与p2
                pre = p2
                p2 = p2.next
        if p1 is not None:
            pre.next = p1
        return dummyHead.next


if __name__ == "__main__":
    l1 = Util.createList([1, 2, 4, 6, 7, 8, 9])
    l2 = Util.createList([1, 3, 5])
    l1 = Util.createList([5])
    l2 = Util.createList([1, 2, 3, 4])
    head = Solution().mergeTwoLists(l1, l2)
    Util.printList(head)
