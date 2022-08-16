'''
给定两个非空链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储单个数字。将这两数相加会返回一个新的链表。
你可以假设除了数字 0 之外，这两个数字都不会以零开头。

链接：https://leetcode-cn.com/problems/add-two-numbers-ii
'''
import Util


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # O(m+n) 104ms 46.97%
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = self.link2num(l1)
        num2 = self.link2num(l2)
        numSum = num1 + num2
        print(num1, '+', num2, '=', numSum)
        return self.num2link(numSum)

    def link2num(self, l):
        cur, ret = l, 0
        while cur is not None:
            ret = ret * 10 + cur.val
            cur = cur.next
        return ret

    def num2link(self, num):
        cur = head = ListNode(None)
        nums = list(str(num))
        for one in nums:
            cur.next = ListNode(one)
            cur = cur.next
        return head.next


if __name__ == "__main__":
    l1 = Util.createList([2, 3])
    l2 = Util.createList([1, 2, 3])
    res = Solution().addTwoNumbers(l1, l2)
    Util.printList(res)
