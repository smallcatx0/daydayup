package leetcode

import (
	"fmt"
	"sort"
	"testing"
)

func sortByBits(arr []int) []int {
	m := make([]int, len(arr))
	for i, v := range arr {
		m[i] = bitsCount(v)*10e5 + v
	}
	sort.Ints(m)
	for i, v := range m {
		arr[i] = v % 1e5
	}
	return arr
}

func bitsCount(n int) int {
	count := 0
	for n > 0 {
		count += n % 2
		n /= 2
	}
	return count
}

func Test_1356(t *testing.T) {
	arr := []int{0, 1, 2, 3, 4, 5, 6, 7, 8}
	res := sortByBits(arr)
	fmt.Println(res)
	fmt.Printf("%b, %d\n", 7, bitsCount(7))
}
