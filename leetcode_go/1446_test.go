package leetcode

import (
	"fmt"
	"testing"
)

func maxPower(s string) int {
	i, p, ml := 0, 0, 1
	for ; i < len(s); i++ {
		if s[p] != s[i] {
			if ml < i-p {
				ml = i - p
			}
			p = i
		}
	}
	if ml < i-p {
		ml = i - p
	}
	return ml
}

func Test_1446(t *testing.T) {
	s := "q"
	res := maxPower(s)
	fmt.Println(res)
}
