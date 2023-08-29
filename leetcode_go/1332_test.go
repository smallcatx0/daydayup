package leetcode

import (
	"fmt"
	"testing"
)

// 我是傻逼
// 判断,是否为回文数
//  是  return 1 否 return 2
func removePalindromeSub(s string) int {
	i, j := 0, len(s)-1
	for i < j {
		if s[i] != s[j] {
			return 2
		}
		i++
		j--
	}
	return 1
}

func Test_1332(t *testing.T) {
	s := "baabb"
	res := removePalindromeSub(s)
	fmt.Println(res)
}
