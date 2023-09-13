package leetcode

import (
	"fmt"
	"testing"
)

func removeDuplicates_26(nums []int) int {
	i, j := 1, 1
	for ; i < len(nums); i++ {
		if nums[i-1] != nums[i] {
			nums[j] = nums[i]
			j++
		}
	}
	return j
}

func Test_26(t *testing.T) {
	nums := []int{1, 1, 1, 2, 2, 3}
	res := removeDuplicates_26(nums)
	fmt.Println(nums[:res])
}
