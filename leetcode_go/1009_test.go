package leetcode

import (
	"fmt"
	"testing"
)

func bitwiseComplement(n int) int {
	res := 0
	bits := make([]int, 0)
	for n > 0 {
		bits = append(bits, inv(n%2))
		n = n / 2
	}
	// fmt.Println(bits)
	st0 := true
	for i := len(bits) - 1; i >= 0; i-- {
		if st0 && bits[i] == 0 {
			continue
		}
		st0 = false
		res = res*2 + bits[i]
	}
	return res
}
func inv(b int) int {
	if b != 0 {
		return 0
	} else {
		return 1
	}
}
func Test_1009(t *testing.T) {
	n := 10
	res := bitwiseComplement(n)
	fmt.Println(res)
}
