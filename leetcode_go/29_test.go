package leetcode

import (
	"fmt"
	"math"
	"testing"
)

func divide(dividend int, divisor int) int {
	if divisor == 1 {
		return dividend
	}
	if divisor == -1 {
		if dividend == math.MinInt32 {
			return math.MaxInt32
		}
		return -dividend
	}
	flag := false
	if divisor > 0 {
		divisor = -divisor
		flag = !flag
	}
	if dividend > 0 {
		dividend = -dividend
		flag = !flag
	}
	n := 0
	for dividend <= divisor {
		i, d := 1, divisor
		for d > -1e9 && dividend <= d+d {
			i += i
			d += d
		}
		n += i
		dividend -= d
	}
	if flag {
		return -n
	} else {
		return n
	}
}

func Test_29(t *testing.T) {
	res := divide(-2147483648, -3)
	fmt.Println(res)

}
