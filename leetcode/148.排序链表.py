#
# @lc app=leetcode.cn id=148 lang=python3
#
# [148] 排序链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if(head == None):
            return None
        dyHead = ListNode(None)
        dyHead.next = head
        curr = head
        while curr.next :
            if curr.val > curr.next.val:
                tmpNode = curr.next
                curr.next = curr.next.next
                curr2 = dyHead
                while curr2.next.val < tmpNode.val :
                    curr2 = curr2.next
                tmpNode.next =curr2.next
                curr2.next = tmpNode
            else:
                curr = curr.next
        return dyHead.next
        
# @lc code=end

if __name__ == "__main__":
    arr = [1,2,3,4]
    linked = curr = ListNode(arr[0])
    for one in arr[1:]:
        curr.next = ListNode(one)
        curr = curr.next
    res = Solution().sortList(linked)
    while res:
        
        res = res.next