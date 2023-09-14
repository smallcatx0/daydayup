package leetcode

import (
	"fmt"
	"testing"
)

func rotate(nums []int, k int) {
	l := len(nums)
	k = k % l
	re := make([]int, k)
	copy(re, nums[l-k:])
	fmt.Println(re)
	for i := 1; i <= l-k; i++ {
		nums[l-i] = nums[l-i-k]
	}
	copy(nums[:k], re)
}

// 反转数组
func rotate_2(nums []int, k int) {
	k = k % len(nums)
	rv(nums)
	rv(nums[:k])
	rv(nums[k:])
}

func rv(nums []int) {
	for i, n := 0, len(nums); i < n/2; i++ {
		nums[i], nums[n-i-1] = nums[n-i-1], nums[i]
	}
}

func Test_189(t *testing.T) {
	nums := []int{1, 2, 3, 4, 5, 6, 7}
	k := 2
	rotate_2(nums, k)
	fmt.Println(nums)
}
