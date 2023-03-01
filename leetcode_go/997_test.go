package leetcode

import (
	"fmt"
	"testing"
)

func findJudge(n int, trust [][]int) int {
	in := make([]int, n+1)
	out := make([]int, n+1)
	for _, v := range trust {
		in[v[1]]++
		out[v[0]]++
	}
	for i := 1; i < n+1; i++ {
		if in[i] == n-1 && out[i] == 0 {
			return i
		}
	}
	return -1
}

func Test_997(t *testing.T) {
	trust := [][]int{
		{1, 3},
		{2, 3},
	}
	res := findJudge(3, trust)
	fmt.Println(res)
}
