package leetcode

import (
	"fmt"
	"testing"
)

func majorityElement(nums []int) int {
	m := map[int]int{}
	for _, v := range nums {
		m[v]++
		if m[v] > len(nums)/2 {
			return v
		}
	}
	return 0
}

func Test_169(t *testing.T) {
	nums := []int{2, 2, 1, 1, 1, 2, 2}
	res := majorityElement(nums)
	fmt.Println(res)
}
