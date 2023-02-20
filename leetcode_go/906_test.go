package leetcode

import (
	"fmt"
	"testing"
)

func smallestRangeI(nums []int, k int) int {
	min, max := int(10e5), -1
	for _, v := range nums {
		if min > v {
			min = v
		}
		if max < v {
			max = v
		}
	}
	ret := (max - k) - (min + k)
	if ret < 0 {
		return 0
	} else {
		return ret
	}
}

func Test_906(t *testing.T) {
	nums := []int{0, 3, 10} // 3, 3, 7
	k := 3
	res := smallestRangeI(nums, k)
	fmt.Println(res)
}
