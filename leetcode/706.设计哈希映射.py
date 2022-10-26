

from typing import List

class node:
    def __init__(self, k,v) -> None:
        self.k = k
        self.v = v
        self.next:node = None

class MyHashMap:

    def __init__(self, cap = 777):
        self.mod = cap
        self.len = 0
        self._data:List[node] = [None]*self.mod

    def put(self, key: int, value: int) -> None:
        self.len += 1
        if self.len > self.mod*2:
            self.rebuild()
        i = key % self.mod
        n = node(key, value)
        curr = self._data[i]
        if curr == None:
            self._data[i] = n
            return
        # 挂到链表尾部
        pre = curr.next
        while curr != None:
            if curr.k == key:
                curr.v = value
                return
            curr = curr.next
            pre = curr
        pre.next = n

    def get(self, key: int) -> int:
        i = key % self.mod
        curr = self._data[i]
        if curr == None:
            return -1
        while curr != None:
            if curr.k == key:
                return curr.v
            curr = curr.next
        return -1

    def remove(self, key: int) -> None:
        i = key % self.mod
        curr = self._data[i]
        if curr == None:
            return
        if curr.k == key:
            self._data[i] = curr.next
            del(curr)
            return
        pre = curr
        curr = curr.next
        while curr != None:
            if curr.k == key:
                pre.next = curr.next
                self.len -= 1
                del(curr)
                return

    def rebuild(self):
        old = self._data
        if self.len >= 10**4:
            self.mod = self.len + 10*4
        else:
            self.mod = self.len * 2
        self._data = [None] * self.mod
        for curr in old:
            if curr == None:
                continue
            while curr != None:
                self.put(curr.k, curr.v)
                curr = curr.next

if __name__ == '__main__':
    h = MyHashMap()
    h.put(1,1)
    h.put(2,2)
    print(h.get(1))
    print(h.get(3))
    h.put(2,1)
    print(h.get(2))
    h.remove(2)
    print(h.get(2))