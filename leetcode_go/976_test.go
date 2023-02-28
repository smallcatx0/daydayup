package leetcode

import (
	"fmt"
	"sort"
	"testing"
)

func largestPerimeter(nums []int) int {
	// 倒叙排序 找相邻的三个
	// sort.Sort(sort.IntSlice(nums))
	sort.Slice(nums, func(i, j int) bool {
		return nums[i] > nums[j]
	})
	for i := 0; i < len(nums)-2; i++ {
		if nums[i] < nums[i+1]+nums[i+2] {
			return nums[i] + nums[i+1] + nums[i+2]
		}
	}
	return 0
}

func Test_976(t *testing.T) {
	nums := []int{1, 2, 1, 10}
	res := largestPerimeter(nums)
	fmt.Println(res)
}
