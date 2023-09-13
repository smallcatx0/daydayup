package leetcode

import (
	"fmt"
	"testing"
)

func createTargetArray(nums []int, index []int) []int {
	ret := make([]int, len(nums))
	for i, v := range index {
		copy(ret[v+1:], ret[v:])
		ret[v] = nums[i]
	}
	return ret
}

func Test_1389(t *testing.T) {
	nums := []int{0, 1, 2, 3, 4}
	index := []int{0, 1, 2, 2, 1}
	ret := createTargetArray(nums, index)
	fmt.Println(ret)

}
