package leetcode

import (
	"fmt"
	"testing"
)

func minStartValue(nums []int) int {
	st, s := 0, 0
	for _, v := range nums {
		s += v
		if s < 1 {
			st += 1 - s
			s = 1
		}
	}
	if st == 0 {
		return 1
	}
	return st
}

func Test_1413(t *testing.T) {
	nums := []int{-3, 2, -3, 4, 2}
	res := minStartValue(nums)
	fmt.Println(res)
}
