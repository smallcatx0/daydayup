package leetcode

import (
	"fmt"
	"testing"
)

func prefixesDivBy5(nums []int) []bool {
	n := 0
	ret := make([]bool, len(nums))
	can := map[int]bool{0: true, 5: true}
	for i, v := range nums {
		n = (n*2 + v) % 10 // 溢出
		ret[i] = can[n]

	}
	return ret
}

func Test_1018(t *testing.T) {
	nums := []int{1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0}
	res := prefixesDivBy5(nums)
	fmt.Println(res)
}
