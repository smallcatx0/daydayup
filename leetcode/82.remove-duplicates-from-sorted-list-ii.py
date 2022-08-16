'''
给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中没有重复出现的数字
'''
import Util


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # O(n) 48ms 94.63%
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        dummyHead = ListNode(None)
        dummyHead.next = head
        pre, cur = dummyHead, dummyHead.next
        while cur is not None and cur.next is not None:
            if cur.next.val == cur.val:
                delVal = cur.val
                # 删掉接下来所有值为delVal的节点
                while cur is not None and cur.val == delVal:
                    delNode = cur
                    cur = cur.next
                    pre.next = delNode.next
                    del delNode
            else:
                pre = cur
                cur = cur.next
        return dummyHead.next


if __name__ == "__main__":
    head = Util.createList([1, 1, 2, 2, 3, 4, 4, 5])
    head = Util.createList([1, 1])
    head = Solution().deleteDuplicates(head)
    Util.printList(head)
