package leetcode

import (
	"fmt"
	"testing"
)

func isMonotonic(nums []int) bool {
	if len(nums) <= 2 {
		return true
	}
	for i := 2; i < len(nums); i++ {

	}
	return false
}

func Test_896(t *testing.T) {
	nums := []int{1, 2, 3}
	ret := isMonotonic(nums)
	fmt.Println(ret)
}
