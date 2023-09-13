package leetcode

import (
	"fmt"
	"testing"
)

func removeDuplicates_80(nums []int) int {
	l := len(nums)
	if l <= 2 {
		return l
	}
	fast, slow := 2, 2
	for fast < l {
		if nums[slow-2] != nums[fast] {
			nums[slow] = nums[fast]
			slow++
		}
		fast++
	}
	return slow
}

func Test_80(t *testing.T) {
	nums := []int{0, 0, 1, 1, 1, 1, 2, 3, 3}
	res := removeDuplicates_80(nums)
	fmt.Println(nums[:res])
}
