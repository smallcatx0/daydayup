package leetcode

import (
	"fmt"
	"testing"
)

// 从最后一位开始找,最小的能到当前的值
func jump(nums []int) int {
	mp := len(nums) - 1
	cnt := 0
	for mp != 0 {
		i, j := len(nums)-2, mp
		for ; i >= 0; i-- {
			if nums[i] >= (j - i) {
				mp = i

			}
		}
		cnt++
	}
	return cnt
}

func Test_45(t *testing.T) {
	nums := []int{2, 3, 0, 1, 4}
	res := jump(nums)
	fmt.Println(res)
}
