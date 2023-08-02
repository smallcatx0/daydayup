package leetcode

import (
	"fmt"
	"testing"
)

// 最大公因子串
func gcdOfStrings(str1 string, str2 string) string {
	if str1+str2 != str2+str1 {
		return ""
	}
	i := gcd(len(str1), len(str2))
	return str1[:i]
}

// 最大公因数
func gcd(a int, b int) int {
	for a != 0 {
		a, b = b%a, a
	}
	return b
}

func Test_1071(t *testing.T) {
	str1 := "ABABAB"
	str2 := "ABAB"
	res := gcdOfStrings(str1, str2)
	fmt.Println(res)

	fmt.Println(gcd(6, 5))
}
