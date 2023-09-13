package leetcode

import (
	"fmt"
	"testing"
)

func removeElement(nums []int, val int) int {
	i, j := 0, 0
	for ; j < len(nums); j++ {
		if nums[j] != val {
			nums[i] = nums[j]
			i++
		}
	}
	return i
}

func Test_27(t *testing.T) {
	nums := []int{3, 2, 2, 3}
	val := 3
	l := removeElement(nums, val)
	fmt.Println(l, nums[:l])
}
