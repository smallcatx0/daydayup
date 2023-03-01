package leetcode

import (
	"fmt"
	"testing"
)

func largestLocal(grid [][]int) [][]int {
	n := len(grid)
	ret := make([][]int, n-2)
	for x := 1; x < n-1; x++ {
		ret[x-1] = make([]int, n-2)
		for y := 1; y < n-1; y++ {
			ret[x-1][y-1] = rangMax(grid, x, y)
		}
	}
	return ret
}

func rangMax(grid [][]int, x, y int) int {
	a := []int{-1, 0, 1}
	max := grid[x][y]
	for _, dx := range a {
		for _, dy := range a {
			if grid[x+dx][y+dy] > max {
				max = grid[x+dx][y+dy]
			}
		}
	}
	return max
}
func Test_2373(t *testing.T) {
	grid := [][]int{
		{9, 9, 8, 1},
		{5, 6, 2, 6},
		{8, 2, 6, 4},
		{6, 2, 2, 2},
	}
	ret := largestLocal(grid)
	fmt.Println(ret)
}
