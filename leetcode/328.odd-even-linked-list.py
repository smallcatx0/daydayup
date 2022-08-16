'''
给定一个单链表，把所有的奇数节点和偶数节点分别排在一起。请注意，这里的奇数节点和偶数节点指的是节点编号的奇偶性，而不是节点的值的奇偶性。
'''
import Util


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # O(n) 48ms 97%
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        sep, pre, cur = head, head, head.next
        i = 2
        while cur is not None:
            if i % 2:  # 当前节点为奇数，移动当前节点到分割节点后，分割节点后移一位
                moveNode = cur
                pre.next = cur.next
                cur = cur.next
                tmp = sep.next
                sep.next = moveNode
                moveNode.next = tmp
                sep = moveNode
            else:
                pre = cur
                cur = cur.next
            i += 1
        return head


if __name__ == "__main__":
    head = Util.createList([1, 2, 3, 4, 5, 6])
    head = Solution().oddEvenList(head)
    Util.printList(head)
