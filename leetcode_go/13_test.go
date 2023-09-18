package leetcode

import (
	"fmt"
	"testing"
)

var romaMapp = map[byte]int{
	'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
}

func romanToInt(s string) int {
	num := romaMapp[s[len(s)-1]]
	for i := len(s) - 2; i >= 0; i-- {
		if romaMapp[s[i]] < romaMapp[s[i+1]] {
			num += -romaMapp[s[i]]
		} else {
			num += romaMapp[s[i]]
		}
	}
	return num
}

func Test_13(t *testing.T) {
	s := "MCMXCIV"
	s = "LVIII"
	res := romanToInt(s)
	fmt.Println(res)
}
