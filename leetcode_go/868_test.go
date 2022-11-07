package leetcode

import (
	"fmt"
	"testing"
)

func binaryGap(n int) int {
	maxl := 0
	st, i := -1, 0
	for n > 0 {
		b := n % 2
		// 找起点
		if st == -1 {
			if b == 1 {
				st = i
			}
		} else {
			// 找终点
			if b == 1 {
				if i-st > maxl {
					maxl = i - st
				}
				st = i
			}
		}
		n = n / 2
		i += 1
	}
	return maxl
}

func Test_868(t *testing.T) {
	n := 9
	ret := binaryGap(n)
	fmt.Println("ret", ret)
}
