'''
反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

说明:
1 ≤ m ≤ n ≤ 链表长度。

示例:

输入: 1->2->3->4->5->NULL, m = 2, n = 4
输出: 1->4->3->2->5->NULL

链接：https://leetcode-cn.com/problems/reverse-linked-list-ii
'''
import Util


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # O(n) 32ms 99.48%
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        i = 1
        cur, pre = head, None
        start, end, midStart = None, None, None
        while cur is not None:
            nextP = cur.next
            if i == m:
                start = pre
                midStart = cur
            if i >= m and i < n:
                cur.next = pre
            elif i >= n:
                cur.next = pre
                break
            pre = cur
            cur = nextP
            i += 1
        if start is None:
            head = cur
        else:
            start.next = cur
        midStart.next = nextP
        return head


if __name__ == "__main__":
    head = Util.createList([1, 2, 3, 4, 5, 6])
    head = Solution().reverseBetween(head, 1, 6)
    Util.printList(head)
