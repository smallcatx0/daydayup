'''
反转一个链表
'''
import Util


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # O(n) 52ms 75%
    def reverseList(self, head: ListNode) -> ListNode:
        pre, cur = None, head
        while cur is not None:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    head = Util.createList(nums)
    Util.printList(head)
    head = Solution().reverseList(head)
    Util.printList(head)
