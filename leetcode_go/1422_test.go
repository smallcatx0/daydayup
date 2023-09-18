package leetcode

import (
	"fmt"
	"testing"
)

func maxScore(s string) int {
	n := int('1' - s[0])
	for _, v := range s[1:] {
		if v == '1' {
			n++
		}
	}
	fmt.Println(n)
	max := n
	for i := 1; i < len(s)-1; i++ {
		fmt.Println(n, max)
		if s[i] == '0' {
			n += 1
		} else {
			n -= 1
		}
		if max < n {
			max = n
		}
	}
	return max
}

func Test_1422(t *testing.T) {
	s := "011101"
	s = "11111"
	// s = "00"
	res := maxScore(s)
	fmt.Println(res)
}
