package leetcode

import (
	"fmt"
	"testing"
)

func freqAlphabets(s string) string {
	// i := 0
	// // for {

	// // }
	return ""
}
func decode(s string) rune {
	if len(s) == 1 {
		fmt.Println(s[0] - '1' + 'a')
		// return s[0] - '0' + 'a'
	}
	return ' '
}

func Test_1309(t *testing.T) {
	s := "10#11#12"
	res := freqAlphabets(s)
	fmt.Println(res)

	fmt.Println(decode("1"))
}
