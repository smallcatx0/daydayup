package leetcode

import (
	"fmt"
	"testing"
)

func canThreePartsEqualSum(arr []int) bool {
	s, l := 0, 0
	for i, v := range arr {
		if v != 0 {
			arr[l] = arr[i]
			l++
		}
		s += v
	}
	if s%3 != 0 {
		return false
	}
	s = s / 3 // 每块大小
	n, k := 0, 0
	for i := 0; i < l; i++ {
		if n == 0 {
			k++
			n = s
			if k == 3 {
				return true
			}
		}
		n -= arr[i]
	}
	return n == 0
}

func Test_1013(t *testing.T) {
	// arr := []int{0, 2, 1, -6, 6, 7, 9, -1, 2, 0, 1}
	// arr := []int{10, -7, 13, -14, 30, 16, -3, -16, -27, 27, 19}
	arr := []int{1, -1, 1, -1}
	// 10,-7,13  -14,30, 16, 0
	res := canThreePartsEqualSum(arr)
	fmt.Println(res)
}
