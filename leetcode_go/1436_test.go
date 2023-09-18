package leetcode

import (
	"fmt"
	"testing"
)

// 起点没出现过
func destCity(paths [][]string) string {
	end := map[string]int{}
	start := map[string]int{}
	for _, v := range paths {
		end[v[1]]++
		start[v[0]]++
	}
	for k := range end {
		if start[k] == 0 {
			return k
		}
	}
	return ""
}

func Test_1436(t *testing.T) {
	paths := [][]string{{"London", "New York"}, {"New York", "Lima"}, {"Lima", "Sao Paulo"}}
	res := destCity(paths)
	fmt.Println(res)
}
