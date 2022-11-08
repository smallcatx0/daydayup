package leetcode

import (
	"fmt"
	"testing"
)

func projectionArea(grid [][]int) int {
	// xy面 = 柱子的个数
	// yz面 = sum({y:0~ed,x_max})
	// xz面 = sum({y_max,x:0~ed})
	xEd, yEd := len(grid), len(grid[0])
	sum := 0
	for i := 0; i < xEd; i++ {
		max := -1
		for j := 0; j < yEd; j++ {
			if grid[i][j] != 0 {
				sum += 1
			}
			if grid[i][j] > max {
				max = grid[i][j]
				// fmt.Printf("%d(%d,%d) ", grid[i][j], i, j)
			}
		}
		// fmt.Println("| max =", max)
		sum += max
	}
	// fmt.Println(sum)
	for i := 0; i < yEd; i++ {
		max := -1
		for j := 0; j < xEd; j++ {
			if grid[j][i] > max {
				max = grid[j][i]
				// fmt.Printf("%d(%d,%d) ", grid[i][j], i, j)
			}
		}
		// fmt.Println("| max =", max)
		sum += max
	}
	return sum
}

func Test_883(t *testing.T) {
	grid := [][]int{{1, 0}, {0, 2}}
	ret := projectionArea(grid)
	fmt.Println(ret)
}
