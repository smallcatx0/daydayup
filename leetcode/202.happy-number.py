class Solution:
    def isHappy(self, n: int) -> bool:
        history = set([n])
        while n != 1:
            # print(n)
            n = self.squ(n)
            if n in history:
                return False
            else:
                history.add(n)
        return True

    def squ(self, num):
        ret = 0
        while num != 0:
            ret += (num % 10)**2
            num = num // 10
        return ret

    def isHappy2(self, n: int) -> bool:
        history = set([n])
        while n != 1:
            nArr = list(str(n))
            n = 0
            for num in nArr:
                n += int(num) ** 2
            if n in history:
                return False
            else:
                history.add(n)
        return True


if __name__ == "__main__":
    n = 19
    res = Solution().isHappy(n)
    print(res)
    res = Solution().isHappy2(n)
    # res = Solution().squ(19)
    print(res)

