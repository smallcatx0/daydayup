class Solution:
    printStrs = "XY01234567890"
    def printN(self, N):
        mid = (N + 1) // 2
        for i in range(1, mid + 1):
            print(self.getLine(i, N))
        for i in range(mid, N):
            print(self.getLine(N - i, N))
        
    def getLine(self, i, N):
        resStr = ['X' for one in range(N)]
        j= 0
        while j < i:
            resStr[j] = resStr[N-j-1] = self.printStrs[j]
            j += 1
        end = N - j -1
        while j <= end:
            resStr[j] = resStr[j-1]
            j += 1
        return resStr
    
    def printN2(self, N):
        strList = "XY0123456789"
        mid = (N + 1) // 2
        for i in range(1, mid + 1):
            for j in range(1, mid + 1):
                print(strList[min(i, j) - 1], end=' ')
                # print((i,j),end='')
            for j in range(mid, N):
                print(strList[min(i, N - j) - 1], end=' ')
                # print((i, N-j), end='')
            print()
        for i in range(mid, N):
            for j in range(1, mid + 1):
                print(strList[min(N - i, j) - 1], end=' ')
                # print((N-i,j),end='')
            for j in range(mid, N):
                print(strList[min(N -i, N-j) - 1], end = ' ')
                # print((N - i, N-j), end='')
            print()
        
        
if __name__ == "__main__":
    Solution().printN2(19)
    # Solution().printN(20)
    # print(Solution().getLine(1, 6))
    # print(Solution().getLine(2, 6))
    # print(Solution().getLine(3, 6))
    # print(Solution().getLine(3, 6))
    # print(Solution().getLine(2, 6))
    # print(Solution().getLine(1, 6))


""" 
1 > X X X X X X
2 > X Y Y Y Y X 
3 > X Y 0 0 Y X
4 > X Y 0 0 Y X
5 > X Y Y Y Y X
6 > X X X X X X
"""