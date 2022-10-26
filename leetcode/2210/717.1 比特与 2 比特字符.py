from typing import List


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i,l = 0, len(bits)
        while i < l - 1:
            if bits[i] == 1:
                i += 2
            else:
                i += 1
        return i == l-1

if __name__ == '__main__':
    bits = bits = [1, 0,1, 0]
    ret = Solution().isOneBitCharacter(bits)
    assert ret == True