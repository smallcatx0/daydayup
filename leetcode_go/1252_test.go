package leetcode

import (
	"fmt"
	"testing"
)

func oddCells(m int, n int, indices [][]int) int {
	rows := make([]int, m)
	cols := make([]int, n)
	for _, v := range indices {
		rows[v[0]]++
		cols[v[1]]++
	}
	count := 0
	for _, r := range rows {
		for _, c := range cols {
			count += (r + c) % 2
		}
	}
	return count
}

func Test_1252(t *testing.T) {
	m, n := 2, 3
	indices := [][]int{{0, 1}, {1, 1}}

	res := oddCells(m, n, indices)
	fmt.Println(res)

}
