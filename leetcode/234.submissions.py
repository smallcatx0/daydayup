'''
请判断一个链表是否为回文链表
'''
import Util


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # O(n) O(1) 72ms 98.15%
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True
        p = q = head
        t = 2
        # 找出前中点
        while q is not None:
            if t == 0:
                p, t = p.next, 2
            q = q.next
            t -= 1
        # 反转后半截
        rightHalf = self.reverseList(p.next)
        # 比较两个链表
        p, q = head, rightHalf
        while q is not None:
            if p.val != q.val:
                return False
            p = p.next
            q = q.next
        return True

    def reverseList(self, head: ListNode) -> ListNode:
        pre, cur = None, head
        while cur is not None:
            nextP = cur.next
            cur.next = pre
            pre = cur
            cur = nextP
        return pre


if __name__ == "__main__":
    head = Util.createList([1, 2, 1])
    res = Solution().isPalindrome(head)
    print(res)
