#! python3

'''
https://leetcode.cn/problems/flood-fill/
'''

from typing import *

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if len(image) == 0:
            return image
        self.image = image
        self.l, self.r = len(image), len(image[0])
        self.old = image[sr][sc]
        self.color = color
        if self.old == self.color:
            return self.image
        self.fill(sr, sc)
        return self.image

    def fill(self, x:int, y:int):
        # 判断坐标是否合法
        if x <0 or x > self.l-1:
            return
        if y <0 or y > self.r -1:
            return
        # 颜色是否匹配
        if(self.image[x][y] != self.old):
            return
        if(self.image[x][y] == self.color):
            return
        self.image[x][y] = self.color
        # 上下左右
        self.fill(x-1, y)
        self.fill(x+1, y)
        self.fill(x, y+1)
        self.fill(x, y-1)
    


'''
[[0,0,0],[0,0,0]]
0
0
0
'''
if __name__ == '__main__':
    image = [
        [0,0,0],[0,0,0]
    ]
    sr, sc = 0,0
    newColor = 0
    s = Solution()
    ret = s.floodFill(image, sr, sc, newColor)
    print(s.image)