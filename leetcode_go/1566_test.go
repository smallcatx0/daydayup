package leetcode

import (
	"fmt"
	"testing"
)

func containsPattern(arr []int, m int, k int) bool {
	l, count := 0, 1
	for ; l <= len(arr)-m; l++ {
		count = 1
		for i := l + m; i <= len(arr)-m; {
			if arrEq(arr[l:l+m], arr[i:i+m]) {
				count += 1
				if count >= k {
					return true
				}
				i = i + m
			} else {
				break
			}
		}
	}
	return false
}

func arrEq(arr1, arr2 []int) bool {
	for i, v := range arr1 {
		if v != arr2[i] {
			return false
		}
	}
	return true
}

func Test_1566(t *testing.T) {
	arr := []int{1, 2, 3, 1, 2}
	m, k := 2, 2
	res := containsPattern(arr, m, k)
	fmt.Println(res)
}
