'''
给定一个嵌套的整型列表。设计一个迭代器，使其能够遍历这个整型列表中的所有整数。
列表中的项或者为一个整数，或者是另一个列表

输入: [[1,1],2,[1,1]]
输出: [1,1,2,1,1]
'''


class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.data = nestedList

    def next(self):
        """
        :rtype: int
        """
        cur = self.data[0]
        del self.data[0]
        while isinstance(cur, list) and len(cur) != 0:
            back = cur[1:]
            self.data = back + self.data
            cur = cur[0]
        if isinstance(cur, list) and len(cur) == 0 and self.hasNext():
            cur = self.next()
        return cur

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.data) != 0


if __name__ == "__main__":
    mlist = [[1, [], 1], 2, [1, 1], [], []]
    i, v = NestedIterator(mlist), []
    while i.hasNext():
        v.append(i.next())
    print(v)
