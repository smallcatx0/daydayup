package leetcode

import (
	"fmt"
	"testing"
)

// 用栈
func makeGood(s string) string {
	if len(s) <= 1 {
		return s
	}
	st := []byte{s[0]}
	for i := 1; i < len(s); i++ {
		if len(st) == 0 {
			st = append(st, s[i])
		} else if isUpLow(st[len(st)-1], s[i]) {
			st = st[:len(st)-1]
		} else {
			st = append(st, s[i])
		}
	}
	return string(st)
}

func isUpLow(c1, c2 byte) bool {
	if c1 > c2 {
		return c1-32 == c2
	}
	return c2-32 == c1
}

func Test_1544(t *testing.T) {
	s := "abBAcaC"
	res := makeGood(s)
	fmt.Println(res)
}
