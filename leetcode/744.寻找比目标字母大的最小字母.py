#! python3

'''
https://leetcode.cn/problems/find-smallest-letter-greater-than-target/
'''


from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # 二分查找
        l,r = 0,len(letters)-1
        if letters[r] < target:
            return letters[0]
        if letters[0] > target:
            return letters[0]
        while l <= r:
            mid = l + (r-l) // 2
            if target < letters[mid]:
                r = mid -1
            else:
                l = mid + 1
        return letters[l%len(letters)]

if __name__ == '__main__':
    l = ["c","f","j"]
    target = "c"
    ret = Solution().nextGreatestLetter(l, target)
    print(ret)