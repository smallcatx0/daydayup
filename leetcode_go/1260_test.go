package leetcode

import (
	"fmt"
	"testing"
)

func shiftGrid(grid [][]int, k int) [][]int {
	count := len(grid) * len(grid[0])
	lines := make([]int, 0, count)
	k = count - (k % count)
	for _, rows := range grid {
		lines = append(lines, rows...)
	}
	x, y := 0, 0
	for _, v := range lines[k:] {
		grid[y][x] = v
		x++
		if x >= len(grid[0]) {
			x, y = 0, y+1
		}
	}
	for _, v := range lines[:k] {
		grid[y][x] = v
		x++
		if x >= len(grid[0]) {
			x, y = 0, y+1
		}
	}
	return grid
}

func Test_1260(t *testing.T) {
	grid := [][]int{
		{1, 2, 3},
		{4, 5, 6},
		{7, 8, 9},
	}
	k := 1
	res := shiftGrid(grid, k)
	fmt.Println(res)
}
