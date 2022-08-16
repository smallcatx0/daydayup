class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.lstrip()
        if len(str) == 0:
            return 0
        res = 0
        flag = 1
        if self.first(str):
            flag,str = self.first(str)
        for c in str:
            if not c.isnumeric():
                break
            res = res * 10 + int(c)
        if flag > 0:
            return min(2**31-1, res)
        elif flag < 0:
            return max(-2**31, flag * res)

    def first(self, str: str)-> int:
        if str[0] == '-':
            return -1 ,str[1:]
        elif str[0] == '+':
            return 1, str[1:]
        else:
            return False

    def myAtoi1(self, str: str) -> int:
        str = str.lstrip()
        res = 0
        flag = True
        sign = 1
        for c in str:
            if flag:
                tmp = self.isHead(c)
                if tmp == False:
                    flag = False
                else: 
                    sign *= tmp
                continue
            if not c.isnumeric():
                break
            res = res * 10 + int(c)
        if sign > 0:
            return min(2**31-1, res)
        elif sign < 0:
            return max(-2**31, sign*res)


    def isHead(self, char) -> int:
        if char == '-':
            return -1
        elif char == '+':
            return 1
        else: 
            return False

if __name__ == "__main__":
    str = "-2147483647"
    res = Solution().myAtoi(str)
    # res = Solution().first(str)
    
    print(res)