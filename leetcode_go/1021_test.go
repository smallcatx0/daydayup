package leetcode

import (
	"bytes"
	"fmt"
	"testing"
)

// 去除最外层有效括号
func removeOuterParentheses(s string) string {
	z := []rune{}
	res := bytes.NewBufferString("")
	for _, c := range s {
		if c == ')' {
			z = z[:len(z)-1]
		}
		if len(z) != 0 {
			res.WriteRune(c)
		}
		if c == '(' {
			z = append(z, c)
		}

	}
	return res.String()
}

func Test_1021(t *testing.T) {
	s := "(()())(())"
	res := removeOuterParentheses(s)
	fmt.Println(res)
}
