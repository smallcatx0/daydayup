class Solution:
    def countAndSay(self, n: int) -> str:
        res, i = '1',1
        while i < n:
            res = self.say(res)
            i += 1
        return res

    def say(self, str):
        num = str[0]
        count = 1
        res = ''
        for c in str[1:]:
            if c == num:
                count += 1
            else:
                res += "%s%s"%(count,num)
                num = c
                count = 1
        res += "%s%s"%(count,num)
        return res
    
if __name__ == "__main__":
    res = Solution().countAndSay(30)
    # res = Solution().say('1')
    print(res)