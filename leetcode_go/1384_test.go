package leetcode

import (
	"fmt"
	"testing"
)

func findLucky(arr []int) int {
	m := map[int]int{}
	for _, v := range arr {
		m[v]++
	}
	max := -1
	for k, v := range m {
		if k == v && v > max {
			max = v
		}
	}
	return max
}

func Test_1384(t *testing.T) {
	arr := []int{2, 2, 3, 4}
	ret := findLucky(arr)
	fmt.Println(ret)
}
