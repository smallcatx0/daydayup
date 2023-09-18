package leetcode

import (
	"fmt"
	"testing"
)

func lengthOfLastWord(s string) int {
	l := len(s)
	i, q := l-1, -1
	for ; i >= 0; i-- {
		if q == -1 {
			if s[i] != ' ' {
				q = i
				continue
			}
		} else if s[i] == ' ' {
			break
		}
	}
	return q - i
}

func Test_58(t *testing.T) {
	s := "   fly me   to   the moon  "
	res := lengthOfLastWord(s)
	fmt.Println(res)
}
