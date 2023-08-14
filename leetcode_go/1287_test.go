package leetcode

import (
	"fmt"
	"testing"
)

func findSpecialInteger(arr []int) int {
	l := len(arr) / 4
	for i := 0; i < len(arr)-l; i++ {
		if arr[i] == arr[i+l] {
			return arr[i]
		}
	}
	return arr[0]
}

func Test_1287(t *testing.T) {
	// arr := []int{1, 2, 2, 6, 6, 6, 6, 7, 10}
	arr := []int{1, 1, 2, 2, 3, 3, 3, 3}
	res := findSpecialInteger(arr)
	fmt.Println(res)
}
