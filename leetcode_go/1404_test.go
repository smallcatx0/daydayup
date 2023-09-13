package leetcode

import (
	"fmt"
	"testing"
)

func numSteps(s string) int {
	cnt, q := 0, 0
	for i := len(s) - 1; i > 0; i-- {
		n := int(s[i]) - 48 + q
		if n%2 == 0 {
			cnt++
		} else {
			cnt += 2
			n += 1
		}
		q = n / 2
	}
	if q != 0 {
		cnt++
	}
	return cnt
}

func Test_1404(t *testing.T) {
	s := "1101"
	res := numSteps(s)
	fmt.Println(res)
}
