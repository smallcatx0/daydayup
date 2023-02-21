package leetcode

import (
	"fmt"
	"testing"
)

/**
频次统计

从 2 ~ min

*/
func hasGroupsSizeX(deck []int) bool {
	fer := map[int]int{}
	for _, v := range deck {
		fer[v] += 1
	}
	fmt.Println(fer)
	min := int(10e5)
	is2bei := true
	for _, v := range fer {
		if v < 2 {
			return false
		}
		if v%2 != 0 {
			is2bei = false
		}
		if min > v {
			min = v
		}
	}
	if is2bei {
		return true
	}
	for _, v := range fer {
		if v%min != 0 {
			return false
		}
	}
	return true
}

// 1,1,1,1,2,2,2,2,2,2
func Test_914(t *testing.T) {
	deck := []int{1, 1, 1, 1, 2, 2, 2, 2, 2, 2}
	res := hasGroupsSizeX(deck)
	fmt.Println(res)
}
