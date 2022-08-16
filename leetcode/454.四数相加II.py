from typing import *


class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        serchSet = {}
        ret = 0
        for i in range(0, len(C)):
            for j in range(0, len(D)):
                sum = C[i] + D[j]
                if sum in serchSet:
                    serchSet[sum] += 1
                else:
                    serchSet[sum] = 1
        for n1 in A:
            for n2 in B:
                serchKey = 0 - n1 - n2
                if serchKey in serchSet:
                    ret += serchSet[serchKey]
        return ret

if __name__ == "__main__":
    A = [1, 2]
    B = [-2, -1]
    C = [-1, 2]
    D = [0, 2]
    res = Solution().fourSumCount(A, B, C, D)
    print(res)
