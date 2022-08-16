#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# @lc code=start

class Solution:
    def hasCycle1(self, head: ListNode) -> bool:
        # 暴力解法
        nodeMap = {}
        curr = head
        while curr != None:
            if curr in nodeMap.keys():
                return True
            else:
                nodeMap[curr] = 1
            curr = curr.next
        return False
    def hasCycle(self, head: ListNode) -> bool:
        # 快慢指针
        if head == None or head.next == None:
            return False
        slow, fast = head, head.next
        while fast != slow:
            if fast == None or fast.next == None or fast.next.next == None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True

# @lc code=end

