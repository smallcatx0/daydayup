'''
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点
'''
import Util


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # O(n) 44ms 86%
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummyHead = ListNode(None)
        dummyHead.next = head
        p, q = dummyHead, head
        w = 1
        while q is not None:
            if w == n + 1:
                p = p.next
                q = q.next
            else:
                q = q.next
                w += 1
        assert(w == n + 1)
        delNode = p.next
        p.next = delNode.next
        del delNode
        return dummyHead.next


if __name__ == "__main__":
    head = Util.createList([1, 2, 3, 4, 5])
    head = Solution().removeNthFromEnd(head, 7)
    Util.printList(head)
