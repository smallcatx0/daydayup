package leetcode

import (
	"fmt"
	"testing"
)

func merge(nums1 []int, m int, nums2 []int, n int) {
	i := m + n - 1
	m, n = m-1, n-1
	for m >= 0 && n >= 0 {
		if nums1[m] > nums2[n] {
			nums1[i] = nums1[m]
			m--
		} else {
			nums1[i] = nums2[n]
			n--
		}
		i--
	}
	// fmt.Println(nums2[:n+1])
	if n >= 0 {
		copy(nums1[0:i+1], nums2[0:n+1])
	}
}

func Test_88(t *testing.T) {
	num1 := []int{1, 2, 4, 0, 0, 0}
	num2 := []int{-1, 5, 6}
	merge(num1, 3, num2, 3)
	fmt.Println(num1)
}
