package leetcode

import (
	"fmt"
	"testing"
)

func sortedSquares(nums []int) []int {
	numsL := len(nums)
	if numsL == 1 {
		return []int{nums[0] * nums[0]}
	}
	ret := make([]int, numsL)
	// 双指针
	i, j := 0, numsL-1
	var a, b int
	p := numsL - 1
	for i <= j {
		a = nums[i] * nums[i]
		b = nums[j] * nums[j]
		if a >= b {
			ret[p] = a
			i++
		} else {
			ret[p] = b
			j--
		}
		p--
	}
	return ret
}

func Test_977(t *testing.T) {
	nums := []int{-7, -3, 2, 3, 11}
	res := sortedSquares(nums)
	fmt.Println(res)
}
