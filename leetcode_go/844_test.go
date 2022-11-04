package leetcode

import (
	"fmt"
	"testing"
)

func backspaceCompare(s string, t string) bool {
	sb := []byte(s)

	for i := 0; i < len(sb); i++ {
		fmt.Println(string(sb[i]))
	}
	return false
}

func Test_844(t *testing.T) {
	s := "ab##"
	tar := "c##d#"
	ret := backspaceCompare(s, tar)
	fmt.Println(ret)
}
