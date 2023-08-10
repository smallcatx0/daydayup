package leetcode

import (
	"fmt"
	"testing"
)

func checkStraightLine(coordinates [][]int) bool {
	if len(coordinates) <= 2 {
		return true
	}
	dx := coordinates[0][0] - coordinates[1][0]
	dy := coordinates[0][1] - coordinates[1][1]
	for _, v := range coordinates[2:] {
		if dx*(coordinates[0][1]-v[1]) != dy*(coordinates[0][0]-v[0]) {
			return false
		}
	}
	return true
}

func Test_1232(t *testing.T) {
	var points [][]int
	points = [][]int{{1, 2}, {3, 3}, {1, 4}}

	res := checkStraightLine(points)
	fmt.Println(res)
}
