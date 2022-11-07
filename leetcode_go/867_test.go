package leetcode

import (
	"fmt"
	"testing"
)

func transpose(matrix [][]int) [][]int {
	if len(matrix) == 0 {
		return matrix
	}
	ret := [][]int{}
	row, col := len(matrix), len(matrix[0])
	for i := 0; i < col; i++ {
		tmp := []int{}
		for j := 0; j < row; j++ {
			tmp = append(tmp, matrix[j][i])
		}
		ret = append(ret, tmp)
	}
	return ret
}

func Test_867(t *testing.T) {
	matrix := [][]int{
		{1, 2},
		{4, 5},
		{7, 8},
	}
	ret := transpose(matrix)
	fmt.Println(ret)
}
