package leetcode

import (
	"fmt"
	"sort"
	"testing"
)

func largestSumAfterKNegations(nums []int, k int) int {
	// 绝对值排序
	sort.Slice(nums, func(i, j int) bool {
		return absInt(nums[i]) > absInt(nums[j])
	})
	fmt.Println(nums)
	// 负数大于 K
	for i := 0; i < len(nums); i++ {
		if k <= 0 {
			break
		}
		// 负的，将其变为正数
		if nums[i] < 0 {
			nums[i] = -nums[i]
			k--
		}
	}
	if k%2 == 1 {
		nums[len(nums)-1] = -nums[len(nums)-1]
	}
	// 负数小于 K
	sum := 0
	for _, v := range nums {
		sum += v
	}
	return sum
}

func absInt(a int) int {
	if a < 0 {
		return -a
	} else {
		return a
	}
}

func Test_1005(t *testing.T) {
	nums := []int{2, -3, -1, 5, -4}
	k := 2
	res := largestSumAfterKNegations(nums, k)
	fmt.Println(res)
}
