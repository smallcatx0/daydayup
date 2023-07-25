package leetcode

import (
	"fmt"
	"testing"
)

func removeDuplicates(s string) string {
	ret := []byte{}
	p := 0
	s = s + " "
	for i := 0; i < len(s)-1; {
		if s[i+1] == s[i] {
			i++
			continue
		}
		if (i-p)%2 == 0 {
			if len(ret) == 0 {
				ret = append(ret, s[i])
			} else if ret[len(ret)-1] == s[i] {
				ret = ret[:len(ret)-1]
			} else {
				ret = append(ret, s[i])
			}
		}
		fmt.Printf("%d~%d %s\n", p, i, string(s[i]))
		i++
		p = i
	}
	return string(ret)
}

func Test_1047(t *testing.T) {
	s := "baaaaaaaaa"
	ret := removeDuplicates(s)
	fmt.Println(ret)
}
