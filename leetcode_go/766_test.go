package test

import (
	"fmt"
	"testing"
)

/**
{1, 2, 3, 4},
{5, 1, 2, 3},
{9, 5, 1, 2},

(x+1, y+1) = (0, 0) (1, 1) (2, 2) (3, 3)
(x+1, y+1) = (0, 1) (1, 2) (2, 3)
(x+1, y+1) = (0, 2) (1, 3)
(x+1, y+1) = (0, 3)
--
(x+1, y+1) = (1, 0) (2, 1)
(x+1, y+1) = (2, 0)
*/
// 766. 托普利茨矩阵
func isToeplitzMatrix(matrix [][]int) bool {
	if len(matrix) == 0 {
		return true
	}
	l, r := len(matrix), len(matrix[0])
	lz := func(m [][]int, l, r, x, y int) bool {
		n := m[x][y]
		for x < l && y < r {
			if n != m[x][y] {
				return false
			}
			x += 1
			y += 1
		}
		return true
	}
	// 从左往右扫描
	for i := 0; i < r; i++ {
		if !lz(matrix, l, r, 0, i) {
			return false
		}
	}
	// 从上往下扫描
	for i := 1; i < l; i++ {
		if !lz(matrix, l, r, i, 0) {
			return false
		}
	}
	return true
}

func Test_766(t *testing.T) {
	matrix := [][]int{
		{1, 2, 3, 4},
		{5, 1, 2, 3},
		{9, 5, 1, 2},
	}
	matrix = [][]int{
		{1, 2},
		{5, 2},
	}
	ret := isToeplitzMatrix(matrix)
	fmt.Println(ret)
}
