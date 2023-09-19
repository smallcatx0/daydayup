package leetcode

import (
	"fmt"
	"testing"
)

func canBeEqual(target []int, arr []int) bool {
	m := map[int]int{}
	for _, v := range arr {
		m[v]++
	}
	for _, v := range target {
		if m[v] == 0 {
			return false
		}
		m[v]--
		if m[v] == 0 {
			delete(m, v)
		}
	}
	return len(m) == 0
}
func Test_1460(t *testing.T) {
	tar := []int{1, 2, 3, 4}
	arr := []int{4, 1, 3, 2}
	res := canBeEqual(tar, arr)
	fmt.Println(res)
}
