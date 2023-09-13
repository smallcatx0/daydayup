package leetcode

import (
	"fmt"
	"testing"
)

func maximum69Number(num int) int {
	l, i := 1, 0
	for n := num; n > 0; n = n / 10 {
		if n%10 == 6 {
			i = l
		}
		l += 1
	}
	if i == 0 {
		return num
	}
	s := 1
	for j := 0; j < i-1; j++ {
		s *= 10
	}
	fmt.Println(s)
	return num + 3*s
}

func Test_1323(t *testing.T) {
	num := 9996
	res := maximum69Number(num)
	fmt.Println(res)
}
