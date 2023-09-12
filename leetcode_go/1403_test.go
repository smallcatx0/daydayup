package leetcode

import (
	"fmt"
	"sort"
	"testing"
)

func minSubsequence(nums []int) []int {
	sort.Ints(nums)
	sum, mSum := 0, 0
	j := len(nums) - 1
	ret := []int{}
	for i := len(nums) - 1; i >= 0; i-- {
		sum += nums[i]
		if mSum <= sum-mSum {
			mSum += nums[j]
			ret = append(ret, nums[j])
			j--
		}
	}
	return ret
}

func Test_1430(t *testing.T) {
	nums := []int{4, 3, 10, 9, 8}
	res := minSubsequence(nums)
	fmt.Println(res)
}
