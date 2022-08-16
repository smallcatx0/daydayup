'''
给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。
'''
import Util


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # O(n) 56ms 76.99%
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        searchSet = set()
        cur, pre = head, None
        while cur is not None:
            if cur.val in searchSet:
                pre.next = cur.next
            else:
                searchSet.add(cur.val)
                pre = cur
            cur = cur.next
        return head


if __name__ == "__main__":
    head = Util.createList([1, 2, 1, 4, 3, 2])
    head = Util.createList([1, 1, 1, 1, 2])
    head = Solution().deleteDuplicates(head)
    Util.printList(head)
