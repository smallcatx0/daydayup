package leetcode

import (
	"fmt"
	"testing"
)

func generateTheString(n int) string {
	res := make([]byte, n)
	for i := 0; i < n; i++ {
		res[i] = 'a'
	}
	if n%2 == 0 {
		res[0] = 'b'
	}
	return string(res)
}

func Test_1374(t *testing.T) {
	res := generateTheString(5)
	fmt.Println(res)
}
