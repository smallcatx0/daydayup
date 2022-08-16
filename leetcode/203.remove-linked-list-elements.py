'''
删除链表中等于给定值 val 的所有节点。

示例:
输入: 1->2->6->3->4->5->6, val = 6
输出: 1->2->3->4->5
'''
import Util


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    # O(n) 84 ms 78%
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        newHead = ListNode(None)
        newHead.next = head
        cur = newHead
        while cur.next is not None:
            if cur.next.val == val:
                delNode = cur.next
                cur.next = delNode.next
                del delNode
            else:
                cur = cur.next
        return newHead.next


if __name__ == "__main__":
    head, val = Util.createList([1, 2, 3, 4, 5, 6]), 6
    head = Solution().removeElements(head, val)
    Util.printList(head)
