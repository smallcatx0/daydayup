#
# @lc app=leetcode.cn id=409 lang=python3
#
# [409] 最长回文串
#

# @lc code=start
class Solution:
    # 75.38 %(40 ms) 14.81 % (15 MB)
    def longestPalindrome(self, s: str) -> int:
        mapp = {}
        for c in s:
            if c in mapp.keys():
                mapp[c] += 1
            else:
                mapp[c] = 1
        count = 0
        for k in list(mapp.keys()):
            if (mapp[k] % 2) == 0:
                count += mapp[k]
                del mapp[k]
            else:
                mo = mapp[k] // 2
                count += 2*mo
                mapp[k] = 1
        if len(mapp) != 0:
            count += 1
        return count
# @lc code=end

if __name__ == '__main__':
    s = 'civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth'
    res = Solution().longestPalindrome(s)
    print(res)