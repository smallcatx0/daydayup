package leetcode

import (
	"fmt"
	"testing"
)

func countLargestGroup(n int) int {
	m := [37]int{}
	max := 0
	for i := 1; i <= n; i++ {
		s := decSum(i)
		m[s]++
		if m[s] > max {
			max = m[s]
		}
	}
	cnt := 0
	for _, v := range m {
		if v == max {
			cnt++
		}
	}
	return cnt
}

func decSum(n int) int {
	s := 0
	for n > 0 {
		s += n % 10
		n = n / 10
	}
	return s
}
func Test_1399(t *testing.T) {
	ret := countLargestGroup(13)
	fmt.Println(ret)
}
