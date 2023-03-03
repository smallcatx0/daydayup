package leetcode

import (
	"fmt"
	"testing"
)

// https://leetcode.cn/problems/bianry-number-to-string-lcci/
// 浮点数: 0.5 = 1 * 10^-1 = 1*2^-1 = sum(n*2^m)
func printBin(num float64) string {
	// 贪心算法
	m := []float64{0.5, 0.25, 0.125, 0.0625, 0.03125, 0.015625, 0.0078125}
	ret := "0."
	for i := 0; i < 7; i++ {
		if num >= m[i] {
			num -= m[i]
			ret += "1"
		} else if num != 0.0 {
			ret += "0"
		} else {
			break
		}
	}
	if num != 0.0 {
		return "ERROR"
	}
	return ret
}

func Test_iv0502(t *testing.T) {
	n := 0.953125
	res := printBin(n)
	fmt.Println(res)
}
