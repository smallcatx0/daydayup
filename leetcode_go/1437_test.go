package leetcode

import (
	"fmt"
	"testing"
)

func kLengthApart(nums []int, k int) bool {
	if len(nums) == 1 {
		return k == 0
	}
	i := 0
	for i = range nums {
		if nums[i] == 1 {
			break
		}
	}
	for j := i + 1; j < len(nums); j++ {
		if nums[j] == 0 {
			continue
		}
		if j-i > k {
			i = j
		} else {
			return false
		}
	}
	return true
}
func Test_1437(t *testing.T) {
	nums := []int{1, 0, 0, 0, 1, 0, 0, 1}
	k := 2
	res := kLengthApart(nums, k)
	fmt.Println(res)
}
