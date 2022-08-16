# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dyHead = ListNode(None)
        dyHead.next = head
        pre, curl, end = dyHead, head, head
        while n > 0:
            n -= 1
            end = end.next
        while end:
            pre = curl
            curl = curl.next
            end = end.next
        pre.next = curl.next
        return dyHead.next
        
if __name__ == "__main__":
    pass