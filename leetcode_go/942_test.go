package leetcode

import (
	"fmt"
	"testing"
)

func diStringMatch(s string) []int {
	low, high := 0, len(s)
	ret := make([]int, 0, len(s)+1)
	for _, v := range s {
		if v == 'I' {
			ret = append(ret, low)
			low++
		} else {
			ret = append(ret, high)
			high--
		}
	}
	ret = append(ret, high)
	return ret
}

func Test_942(t *testing.T) {
	s := "DDD"
	res := diStringMatch(s)
	fmt.Println(res)
}
