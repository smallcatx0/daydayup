package leetcode

import (
	"fmt"
	"testing"
)

func largeGroupPositions(s string) [][]int {
	l := len(s)
	ret := [][]int{}
	if l < 3 {
		return ret
	}
	st := 0
	for i := 1; i < l; i++ {
		if s[i] == s[st] {
			continue
		}
		// 记录长度
		if i-st >= 3 {
			ret = append(ret, []int{st, i - 1})
		}
		st = i
	}
	if l-st >= 3 {
		ret = append(ret, []int{st, l - 1})
	}
	return ret
}

func Test_830(t *testing.T) {
	s := "aaa"
	ret := largeGroupPositions(s)
	fmt.Println(ret)
}
