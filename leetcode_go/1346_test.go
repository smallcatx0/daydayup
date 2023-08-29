package leetcode

import (
	"fmt"
	"testing"
)

func checkIfExist(arr []int) bool {
	m := make(map[int]int, len(arr))
	for i, v := range arr {
		m[2*v] = i
	}
	for j, v := range arr {
		if i, ok := m[v]; ok && j != i {
			return true
		}
	}
	return false
}

func Test_1346(t *testing.T) {
	arr := []int{-2, 0, 10, -19, 4, 6, -8}
	res := checkIfExist(arr)
	fmt.Println(res)
}
