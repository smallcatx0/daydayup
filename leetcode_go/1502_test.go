package leetcode

import (
	"fmt"
	"sort"
	"testing"
)

// 暴力:先排序后 累加
func canMakeArithmeticProgression(arr []int) bool {
	sort.Ints(arr)
	dt := arr[1] - arr[0]
	for i := 2; i < len(arr); i++ {
		if arr[i]-arr[i-1] != dt {
			return false
		}
	}
	return true
}

func Test_1502(t *testing.T) {
	arr := []int{1, 5, 1}
	ret := canMakeArithmeticProgression(arr)
	fmt.Println(ret)
}
