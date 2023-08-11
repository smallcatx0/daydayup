package leetcode

import (
	"fmt"
	"testing"
)

func minTimeToVisitAllPoints(points [][]int) int {
	d := 0
	for i := 1; i < len(points); i++ {
		// fmt.Println(points[i-1], points[i])
		d += absMax(points[i][0]-points[i-1][0], points[i][1]-points[i-1][1])
	}
	return d
}

func absMax(x, y int) int {
	if x < 0 {
		x = -x
	}
	if y < 0 {
		y = -y
	}
	if x > y {
		return x
	} else {
		return y
	}
}
func Test_1266(t *testing.T) {
	points := [][]int{{1, 1}, {3, 4}, {-1, 0}}
	res := minTimeToVisitAllPoints(points)

	fmt.Println(res)
}
