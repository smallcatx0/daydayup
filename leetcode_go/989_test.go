package leetcode

import (
	"fmt"
	"testing"
)

func addToArrayForm(num []int, k int) []int {
	i := len(num) - 1
	q, s := 0, 0
	for k != 0 || q != 0 {
		if i >= 0 {
			s = q + num[i] + k%10
			num[i] = s % 10
		} else {
			s = q + k%10
			num = append([]int{s % 10}, num...)
		}
		q = s / 10
		k = k / 10
		i--
	}
	// fmt.Println(q)
	return num
}

func Test_989(t *testing.T) {
	nums := []int{9, 9}
	k := 1
	res := addToArrayForm(nums, k)
	fmt.Println(res)
}
