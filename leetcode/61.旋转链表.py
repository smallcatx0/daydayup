#
# @lc app=leetcode.cn id=61 lang=python3
#
# [61] 旋转链表
#
from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# @lc code=start
class Solution:
    #  63.5%(44 ms) 96.36%(14.6 MB)
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head == None:
            return None
        # 计算长度
        pre, curr, lens = None, head, 0
        while curr != None:
            lens += 1
            pre = curr
            curr = curr.next
        # 连成一个环
        pre.next = head
        k = k % lens
        # 截断
        pre, curr = None, head
        for i in range(lens - k):
            pre = curr
            curr = curr.next
        pre.next = None
        return curr 
# @lc code=end

