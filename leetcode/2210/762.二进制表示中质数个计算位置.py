
class Solution:
    _zs = {2:1,3:1,5:1,7:1,11:1,13:1,17:1,19:1}
    def countPrimeSetBits(self, left: int, right: int) -> int:
        ret = 0
        for i in range(left, right+1):
            # print(i)
            if self.bit1(i) in self._zs:
                ret += 1
        return ret
            
        
    def bit1(self, n)->int:
        count = 0
        while n :
            n = n&(n-1)
            count += 1
        return count
            


if __name__ == '__main__':
    left, right = 6,10
    res = Solution().countPrimeSetBits(left, right)
    print(res)