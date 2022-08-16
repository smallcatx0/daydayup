'''
给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。
你应当保留两个分区中每个节点的初始相对位置
'''
import Util


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # O(n) 52ms 65.22%
    def partition(self, head: ListNode, x: int) -> ListNode:
        flag = True
        sep, pre, cur = None, None, head
        while cur is not None:
            if cur.val < x and flag:
                # 找初始到分隔的节点
                sep, pre = cur, cur
                cur = cur.next
                continue
            else:
                flag = False
            if cur.val < x:  # 当前节点比目标值小，移动此节点到分隔节点后
                moveNode = cur
                pre.next = cur.next
                cur = cur.next
                if sep is None:
                    tmp = head
                    head = moveNode
                    moveNode.next = tmp
                    sep = moveNode
                else:
                    tmp = sep.next
                    sep.next = moveNode
                    moveNode.next = tmp
                    sep = moveNode
            else:
                pre = cur
                cur = cur.next
        return head


if __name__ == "__main__":
    head, x = Util.createList([1, 2, 4, 3, 1, 5, 2]), 3
    head, x = Util.createList([2, 1]), 1
    head, x = Util.createList([3, 1, 2]), 3
    head = Solution().partition(head, x)
    Util.printList(head)
