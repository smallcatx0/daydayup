package leetcode

import (
	"fmt"
	"testing"
)

// 从后往前找0
func canJump(nums []int) bool {

	zeroI := -1
	for i := len(nums) - 2; i >= 0; i-- {
		if zeroI == -1 {
			if nums[i] == 0 {
				zeroI = i
			}
		} else {
			// 找到0后 找前面大于当前位置的数
			if nums[i] > zeroI-i {
				zeroI = -1
			}
		}
	}

	return zeroI == -1
}

func Test_55(t *testing.T) {
	nums := []int{3, 2, 1, 0, 4}
	nums = []int{0}
	res := canJump(nums)
	fmt.Println(res)
}
