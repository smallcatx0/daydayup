package leetcode

import (
	"fmt"
	"testing"
)

func decompressRLElist(nums []int) []int {
	res := make([]int, 0, 20)
	for i := 0; i < len(nums); i += 2 {
		for j := 0; j < nums[i]; j++ {
			res = append(res, nums[i+1])
		}
	}
	return res
}

func Test_1313(t *testing.T) {
	nums := []int{1, 1, 2, 3}
	res := decompressRLElist(nums)
	fmt.Println(res)
}
