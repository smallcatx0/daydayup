package leetcode

import (
	"fmt"
	"testing"
)

func replaceElements(arr []int) []int {
	l := len(arr)
	max := arr[l-1]
	arr[l-1] = -1
	if l <= 1 {
		return arr
	}
	for i := l - 2; i >= 0; i-- {
		curr := arr[i]
		arr[i] = max
		if max < curr {
			max = curr
		}
	}
	return arr
}

func Test_1299(t *testing.T) {
	arr := []int{17, 18, 5, 4, 6, 1}
	res := replaceElements(arr)
	fmt.Println(res)
}
