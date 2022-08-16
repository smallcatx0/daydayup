class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        pre, curl, nextNode = None, head, head.next
        while nextNode:
            curl.next = pre
            pre = curl
            curl = nextNode
            nextNode = nextNode.next
        curl.next = pre
        return curl