package leetcode

import (
	"fmt"
	"testing"
)

func numEquivDominoPairs(dominoes [][]int) int {
	cnt := [100]int{}
	ret := 0
	for _, v := range dominoes {
		if v[0] > v[1] {
			v[0], v[1] = v[1], v[0]
		}
		k := v[0]*10 + v[1]
		ret += cnt[k]
		cnt[k]++
	}
	return ret
}

func C(m, n int) int {
	if m < n {
		m, n = n, m
	}
	x, y := 1, 1
	for i := 0; i < n; i++ {
		x = x * (m - i)
		y = y * (n - i)
	}
	return x / y
}

func Test_1128(t *testing.T) {
	dominoes := [][]int{{1, 2}, {2, 1}, {1, 1}, {2, 1}, {5, 6}}
	res := numEquivDominoPairs(dominoes)

	fmt.Println(res)

	// fmt.Println(C(3, 2))
}
