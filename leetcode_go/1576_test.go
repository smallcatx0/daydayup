package leetcode

import (
	"fmt"
	"testing"
)

const Z = "abcdefg"

func modifyString(s string) string {
	s = "?" + s + "?"
	res := []byte(s)
	for i := 1; i < len(res)-1; i++ {
		if res[i] == '?' {
			for j := range Z {
				if Z[j] != res[i-1] && Z[j] != res[i+1] {
					res[i] = Z[j]
				}
			}
		} else {
			res[i] = byte(res[i])
		}
	}
	return string(res[1 : len(res)-1])
}
func Test_1576(t *testing.T) {
	s := "?a??????e"
	res := modifyString(s)
	fmt.Println(res)
}
