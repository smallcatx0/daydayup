package leetcode

import (
	"fmt"
	"testing"
)

func isMonotonic(nums []int) bool {
	if len(nums) <= 2 {
		return true
	}
	op := 0
	for i := 1; i < len(nums); i++ {
		// 先判断单调方向
		if op == 0 {
			if nums[i] > nums[i-1] {
				op = 1
			}
			if nums[i] < nums[i-1] {
				op = -1
			}
		} else {
			fmt.Println(nums[i] - nums[i-1]*op)
			if (nums[i]-nums[i-1])*op < 0 {
				return false
			}
		}
	}
	return true
}

func Test_896(t *testing.T) {
	nums := []int{5, 3, 2, 4, 1}
	ret := isMonotonic(nums)
	fmt.Println(ret)
}
