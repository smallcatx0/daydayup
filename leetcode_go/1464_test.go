package leetcode

import (
	"fmt"
	"testing"
)

func maxProduct(nums []int) int {
	max := [2]int{}
	for _, v := range nums {
		if v > max[0] {
			max[1], max[0] = max[0], v
		} else if v > max[1] {
			max[1] = v
		}
	}
	return (max[0] - 1) * (max[1] - 1)
}

func Test_1464(t *testing.T) {
	nums := []int{2, 3, 5, 8}
	res := maxProduct(nums)
	fmt.Println(res)
}
