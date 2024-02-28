package leetcode

import (
	"fmt"
	"strconv"
	"testing"
)

// 解法一：数字遍历
func thousandSeparator(n int) string {
	if n < 10 {
		return string([]byte{byte('0' + n)})
	}
	res := []byte{}
	i := 0
	for ; n > 0; n = n / 10 {
		x := n % 10
		res = append([]byte{byte(x + 48)}, res...)
		i += 1
		if i >= 3 {
			i = 0
			res = append([]byte{'.'}, res...)
		}
	}
	if res[0] == '.' {
		return string(res[1:])
	}
	return string(res)
}

// 方法二：转化为字符串
func thousandSeparator2(n int) string {
	s := strconv.Itoa(n)
	res := ""
	for ed := len(s); ed > 0; ed -= 3 {
		st := ed - 3
		if st <= 0 {
			st = 0
		}
		res = "." + s[st:ed] + res
	}
	return string(res[1:])
}

func Test_1556(t *testing.T) {
	// fmt.Println(thousandSeparator2(12312))
	fmt.Println(thousandSeparator2(0))
}
