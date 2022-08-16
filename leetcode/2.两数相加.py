#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(None)
        addmun = 0
        cur = res
        while l1 is not None or l2 is not None:
            num1 = num2 = 0
            if l1 is not None:
                num1 = l1.val
                l1 = l1.next
            if l2 is not None:
                num2 = l2.val
                l2 = l2.next
            theSum = num1 + num2 + addmun
            cur.next = ListNode(theSum % 10)
            cur = cur.next
            addmun = theSum // 10
        if addmun != 0:
            cur.next = ListNode(addmun)
        return res.next

# @lc code=end
