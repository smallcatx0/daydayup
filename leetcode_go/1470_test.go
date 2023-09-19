package leetcode

import (
	"fmt"
	"testing"
)

func shuffle(nums []int, n int) []int {
	tmp := make([]int, n)
	copy(tmp, nums[0:n])
	for i, j := 0, 0; i < n; i++ {
		nums[j] = tmp[i]
		nums[j+1] = nums[i+n]
		j += 2
	}
	return nums
}

func shuffle_2(nums []int, n int) []int {
	ret := make([]int, len(nums))
	for i, j := 0, 0; i < n; i++ {
		ret[j] = nums[i]
		ret[j+1] = nums[i+n]
		j += 2
	}
	return ret
}
func Test_1470(t *testing.T) {
	nums := []int{2, 5, 1, 3, 4, 7}
	n := 3
	res := shuffle(nums, n)
	fmt.Println(res)
}
