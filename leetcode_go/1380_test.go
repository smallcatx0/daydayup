package leetcode

import (
	"fmt"
	"testing"
)

func luckyNumbers(matrix [][]int) []int {
	// 暴力吧
	colI := map[int]int{}
	m, n := len(matrix), len(matrix[0])
	for i := 0; i < m; i++ {
		min, minI := int(10e5+1), 0
		for j := 0; j < n; j++ {
			if min > matrix[i][j] {
				min = matrix[i][j]
				minI = j
			}
		}
		if colI[minI] < min {
			colI[minI] = min
		}
	}
	// fmt.Println(colI)
	ret := []int{}
	for j, max := range colI {
		ok := true
		for i := 0; i < m; i++ {
			if max < matrix[i][j] {
				ok = false
				break
			}
		}
		if ok {
			ret = append(ret, max)
		}
	}
	return ret
}

// 在同一行的所有元素中最小, 在同一行的所有元素中最小
func Test_1380(t *testing.T) {
	mat := [][]int{
		{7, 8},
		{1, 2},
	}
	res := luckyNumbers(mat)
	fmt.Println(res)
}
