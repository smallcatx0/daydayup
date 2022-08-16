'''
对链表进行插入排序
'''

import Util


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # O(n^2) 196 ms 91.65%
    def insertionSortList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        dummyHead = ListNode(None)
        dummyHead.next = head
        sep = head
        while sep.next is not None:
            nowNode = sep.next
            if nowNode.val < sep.val:
                sep.next = nowNode.next
                # 移动此节点到前面合适的位置
                cur = dummyHead
                while cur.next.val < nowNode.val:
                    cur = cur.next
                nowNode.next = cur.next
                cur.next = nowNode
            else:
                sep = sep.next
        return dummyHead.next


if __name__ == "__main__":
    head = Util.createList([1, 3, 2, 4])
    head = Util.createList([5, 4, 3, 1])
    head = Util.createList([1, 3, 1, 1])
    head = Util.createList([1])
    head = Solution().insertionSortList(head)
    Util.printList(head)
