# -*- coding: utf-8 -*-
# @Author: tan
# @Date:   2019-09-27 15:28:47
# @Last Modified by:   tan
# @Last Modified time: 2019-09-27 16:46:26
import random


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def orderArray(n):
    '''生成[0 ~ n-1]的有序列表
    '''
    return [i for i in range(0, n)]


def randomArray(length, scope):
    '''生成length个[0 ~ scope]的随机序列
    '''
    return [random.randint(0, scope) for i in range(0, length)]


def createList(arr):
    '''通数组创建链表
    '''
    if len(arr) == 0:
        return None
    cur = head = ListNode(arr[0])
    for one in arr[1:]:
        cur.next = ListNode(one)
        cur = cur.next
    return head


def printList(head):
    '''打印链表
    '''
    cur = head
    i = 100
    while cur is not None:
        print(cur.val, "->", end=' ')
        cur = cur.next
        if i <= 0:
            break
        i -= 1
    print("None")


if __name__ == '__main__':
    # res = orderArray(50)
    res = randomArray(10, 5)
    print(res)
