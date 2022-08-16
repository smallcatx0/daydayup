'''
给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数
'''
import Util


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if k == 0 or head is None:
            return head
        dummyHead = ListNode(None)
        dummyHead.next = head
        p, q = dummyHead, dummyHead.next
        tailNode = None
        linkLen = None
        w = 1
        flag = True
        while w <= k:
            if q.next is None:
                q.next = head
                tailNode = q
                linkLen = w
            if flag and linkLen is not None:
                k = (k - linkLen) % linkLen + linkLen
                print(k)
                flag = False
            q = q.next
            w += 1
        while q != head:
            if q.next is None:
                q.next = head
                tailNode = q
                linkLen = w
            p = p.next
            q = q.next
            w += 1
        # print(linkLen)
        # 旋转链表长度次.链表保持不动
        if p.val is None:
            tailNode.next = None
        else:
            dummyHead.next = p.next
            p.next = None
        return dummyHead.next


if __name__ == "__main__":
    head = Util.createList([1, 2, 3, 4])
    # head = Util.createList([1, 2, 1, 4])
    # head = Util.createList([1])
    for t in range(6):
        head = Solution().rotateRight(head, t)
        Util.printList(head)
