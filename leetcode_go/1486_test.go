package leetcode

import (
	"testing"
)

func xorOperation(n int, start int) int {
	// 先暴力解吧
	ret := start
	for i := 1; i < n; i++ {
		ret = ret ^ (start + 2*i)
	}
	return ret
}

func Test_1486(t *testing.T) {
	res := xorOperation(5, 0)
	println(res)
}
