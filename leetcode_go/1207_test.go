package leetcode

import (
	"fmt"
	"testing"
)

func uniqueOccurrences(arr []int) bool {
	m := map[int]int{}
	for _, v := range arr {
		m[v]++
	}
	mm := map[int]int{}
	for _, v := range m {
		mm[v]++
		if mm[v] >= 2 {
			return false
		}
	}
	return true
}

func Test_1207(t *testing.T) {
	arr := []int{1, 2, 2, 1, 1, 3}
	res := uniqueOccurrences(arr)
	fmt.Println(res)
}
