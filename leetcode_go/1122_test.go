package leetcode

import (
	"fmt"
	"sort"
	"testing"
)

/**
给你两个数组，arr1 和 arr2，arr2 中的元素各不相同，arr2 中的每个元素都出现在 arr1 中。
对 arr1 中的元素进行排序，使 arr1 中项的相对顺序和 arr2 中的相对顺序相同。未在 arr2 中出现过的元素需要按照升序放在 arr1 的末尾。
*/
func relativeSortArray(arr1 []int, arr2 []int) []int {
	arr2Mapp := make(map[int]int, len(arr2))
	for _, v := range arr2 {
		arr2Mapp[v] = 0
	}
	rem := make([]int, 0, len(arr1)-len(arr2))
	for _, v := range arr1 {
		if _, ok := arr2Mapp[v]; ok {
			arr2Mapp[v]++
		} else {
			// 可以用个 插入排序
			rem = append(rem, v)
		}
	}
	sort.Ints(rem)
	i := 0
	for _, v := range arr2 {
		for j := arr2Mapp[v]; j > 0; j-- {
			arr1[i] = v
			i++
		}
	}
	return append(arr1[:i], rem...)
}

func Test_1122(t *testing.T) {
	arr1 := []int{28, 6, 22, 8, 44, 17}
	arr2 := []int{22, 28, 8, 6}
	res := relativeSortArray(arr1, arr2)
	fmt.Println(res)
}
