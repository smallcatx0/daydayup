package leetcode

import (
	"fmt"
	"sort"
	"testing"
)

func kWeakestRows(mat [][]int, k int) []int {
	r := make([]int, len(mat))
	for i := 0; i < len(mat); i++ {
		for _, v := range mat[i] {
			if v == 0 {
				break
			}
			r[i] += 1000
		}
		r[i] += i
	}
	sort.Ints(r)
	ret := make([]int, k)
	for i := 0; i < k; i++ {
		ret[i] = r[i] % 1000
	}
	return ret
}

func Test_1337(t *testing.T) {
	mat := [][]int{
		{1, 1, 0, 0, 0},
		{1, 1, 1, 1, 0},
		{1, 0, 0, 0, 0},
		{1, 1, 0, 0, 0},
		{1, 1, 1, 1, 1},
	}
	res := kWeakestRows(mat, 3)
	fmt.Println(res)
}
