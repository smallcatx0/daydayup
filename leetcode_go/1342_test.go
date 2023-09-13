package leetcode

import (
	"fmt"
	"testing"
)

// 先暴力算吧
func numberOfSteps(num int) int {
	i := 0
	for num > 0 {
		if num%2 == 0 {
			num = num / 2
		} else {
			num = num - 1
		}
		i++
	}
	return i
}

func Test_1342(t *testing.T) {
	num := 14
	res := numberOfSteps(num)
	fmt.Println(res)
}
