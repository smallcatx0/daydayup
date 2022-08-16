

class Solution:
    # TODO: 未完成
    def nearestPalindromic(self, n: str) -> str:
        bft = []  # 存储所有可能解
        sLen = len(n)
        if sLen < 2:  # 一位数的减一
            return str(int(n) - 1)
        if n[0] == '1' and int(n[1:]) == 0:
            # 如果是10,100,100 ...
            return str(int(n) - 1)
        if n == '11':
            return '9'
        s = list(n)
        p, q = self.midTow(sLen)
        notHws = 0
        while p >= 0:
            if s[q] != s[p]:
                s[q] = s[p]
                notHws = 1
            p -= 1
            q += 1
        if notHws:
            # 本身不是回文数
            bft.append(int(''.join(s)))
        else:
            if n[:2] == '10':  # 1001 这种情况
                bft.append(int('9' * (sLen - 1)))
            elif n[:2] == '99':  # 9999 这种情况
                bft.append(int('1' + '0' * (sLen - 1) + '1'))
            # 本身就是回文数，中间点减一或者加一
            bft.extend(self.hwsUpLower(s))
        return bft

    def midTow(self, sLen):
        q = (sLen - 1) // 2 + 1
        if sLen % 2:
            return (q - 2, q)
        else:
            return (q - 1, q)

    def hwsUpLower(self, n):
        ret = []
        nLen = len(n)
        mid = nLen // 2
        if nLen % 2:
            midvalue = int(n[mid])
            if midvalue == 0:
                n[mid] = str(midvalue + 1)
                ret.append(int(''.join(n)))
            elif midvalue == 9:
                n[mid] = str(midvalue - 1)
                ret.append(int(''.join(n)))
            else:
                n[mid] = str(midvalue - 1)
                ret.append(int(''.join(n)))
                n[mid] = str(midvalue + 1)
                ret.append(int(''.join(n)))
        else:
            midvalue1, midvalue2 = int(n[mid - 1]), int(n[mid])
            if midvalue1 == 0:
                n[mid - 1], n[mid] = str(midvalue1 + 1), str(midvalue2 + 1)
                ret.append(int(''.join(n)))
            elif midvalue == 9:
                n[mid - 1], n[mid] = str(midvalue1 - 1), str(midvalue2 - 1)
                ret.append(int(''.join(n)))
            else:
                n[mid - 1], n[mid] = str(midvalue1 - 1), str(midvalue2 - 1)
                ret.append(int(''.join(n)))
                n[mid - 1], n[mid] = str(midvalue1 + 1), str(midvalue2 + 1)
                ret.append(int(''.join(n)))
        return ret

if __name__ == "__main__":
    s = '4'
    s = "1213"
    s = '100'
    s = '990099'
    res = Solution().nearestPalindromic(s)
    # res = Solution().hwsUpLower(list(s))
    print(res)
