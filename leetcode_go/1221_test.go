package leetcode

import (
	"fmt"
	"testing"
)

var RL = map[rune]rune{
	'R': 'L',
	'L': 'R',
}

func balancedStringSplit(s string) int {
	mst := []rune{}
	count := 0
	for _, v := range s {
		if len(mst) == 0 {
			mst = append(mst, v)
			continue
		}
		// 栈顶匹配
		topIndex := len(mst) - 1
		if mst[topIndex] == RL[v] {
			mst = mst[:topIndex]
		} else {
			mst = append(mst, v)
		}
		if len(mst) == 0 {
			count++
		}
	}
	return count
}

func Test_1121(t *testing.T) {
	s := "RLRRRLLRLL"
	res := balancedStringSplit(s)
	fmt.Println(res)
}
