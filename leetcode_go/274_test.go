package leetcode

import (
	"fmt"
	"sort"
	"testing"
)

func hIndex(citations []int) int {
	sort.Ints(citations)
	l := len(citations)
	for i := 1; i <= l; i++ {
		fmt.Println(citations[l-i], i, citations[l-i] >= i)
		if citations[l-i] < i {
			return i - 1
		}
	}
	return l
}

func Test_274(t *testing.T) {
	cit := []int{11, 15}
	res := hIndex(cit)
	fmt.Println(res)
}
