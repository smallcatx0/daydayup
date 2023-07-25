package leetcode

import (
	"fmt"
	"testing"
)

// 三个点，这些点 各不相同 且不在一条直线上 。
/**
x1,y1 x2,y2 x3,y3
(x1-x2)/(y1-y2) = (x1-x3)/(y1-y3)
(x1-x2)*(y1-y3) = (x1-x3)*(y1-y2)
*/
func isBoomerang(points [][]int) bool {
	dx1 := points[0][0] - points[1][0]
	dy1 := points[0][1] - points[1][1]
	dx2 := points[0][0] - points[2][0]
	dy2 := points[0][1] - points[2][1]
	return dx1*dy2 != dx2*dy1
}

func Test_1037(t *testing.T) {
	points := [][]int{{0, 1}, {1, 0}, {0, 2}}
	ret := isBoomerang(points)
	fmt.Println(ret)
}
