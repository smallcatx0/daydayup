package leetcode

import (
	"fmt"
	"sort"
	"testing"
)

func minimumAbsDifference(arr []int) [][]int {
	if len(arr) == 2 {
		if arr[0] > arr[1] {
			arr[0], arr[1] = arr[1], arr[0]
		}
		return [][]int{{arr[0], arr[1]}}
	}
	sort.Ints(arr)
	min := arr[1] - arr[0]
	sts := []int{arr[0]}
	for i := 1; i < len(arr)-1; i++ {
		k := arr[i+1] - arr[i]
		if k < min {
			min = k
			sts = []int{arr[i]}
		} else if k == min {
			sts = append(sts, arr[i])
		}
	}
	sort.Ints(sts)
	ret := [][]int{}
	for _, v := range sts {
		ret = append(ret, []int{v, v + min})
	}
	return ret
}

func Test_1200(t *testing.T) {
	arr := []int{3, 8, -10, 23, 19, -4, -14, 27}
	res := minimumAbsDifference(arr)
	fmt.Println(res)
}
