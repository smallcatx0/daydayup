package leetcode

import (
	"fmt"
	"testing"
)

func restoreString(s string, indices []int) string {
	ret := make([]byte, len(s))
	for i, v := range indices {
		ret[i] = s[v]
	}
	return string(ret)
}

func Test_1528(t *testing.T) {
	s := "codeleet"
	indices := []int{4, 5, 6, 7, 0, 2, 1, 3}
	res := restoreString(s, indices)
	fmt.Println(res)

}
