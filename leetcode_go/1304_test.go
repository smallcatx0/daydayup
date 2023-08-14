package leetcode

import (
	"fmt"
	"testing"
)

func sumZero(n int) []int {
	res := make([]int, n)
	for i := 0; i < n/2; i++ {
		res[i] = n - i
		res[n-i-1] = 0 - res[i]
	}
	return res
}

func Test_1304(t *testing.T) {
	n := 1
	res := sumZero(n)
	fmt.Println(res)
}
