def howManyGood(s)->int:
    ret = 0
    GoodStack = ['d','o','o', 'G']
    for c in s:
        if c == GoodStack[-1]:
            GoodStack.pop()
        if len(GoodStack) == 0:
            ret += 1
            GoodStack = ['d','o','o', 'G']
    return ret

if __name__ == "__main__":
    s = 'GoodGoood'
    res = howManyGood(s)
    print(res)
