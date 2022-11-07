package leetcode

import (
	"fmt"
	"testing"
)

func backspaceCompare(s string, t string) bool {
	return string(Parse(s)) == string(Parse(t))
}

func Parse(s string) []byte {
	b := []byte(s)
	top := 0
	for i := 0; i < len(b); i++ {
		if b[i] == '#' {
			if top != 0 {
				top -= 1
			}
		} else {
			b[top] = b[i]
			top += 1
		}
	}
	// fmt.Println(string(b[:top]))
	return b[:top]
}
func Test_844(t *testing.T) {
	s := "y#fo##f"
	tar := "y#f#o##f"
	ret := backspaceCompare(s, tar)
	fmt.Println(ret)
}
