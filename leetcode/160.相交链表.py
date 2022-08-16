#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# @lc code=start

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA == None or headB == None:
            return None
        pA,pB = headA, headB
        while pA != pB:
            if pA == None:
                pA = headB
            else:
                pA = pA.next
            if pB == None:
                pB = headA
            else:
                pB = pB.next
        return pA
        
# @lc code=end
