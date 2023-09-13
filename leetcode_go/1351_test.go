package leetcode

import (
	"fmt"
	"testing"
)

func countNegatives(grid [][]int) int {
	m, n := len(grid), len(grid[0])
	count := 0
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if grid[i][j] < 0 {
				count += (n - j)
				break
			}
		}
	}
	return count
}

func Test_1351(t *testing.T) {
	grid := [][]int{
		{4, 3, 2, -1},
		{3, 2, 1, -1},
		{1, 1, -1, -2},
		{-1, -1, -2, -3},
	}
	res := countNegatives(grid)
	fmt.Println(res)
}
