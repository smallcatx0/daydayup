package leetcode

import (
	"fmt"
	"testing"
)

func findKthPositive(arr []int, k int) int {
	dt := arr[0] - 1
	if dt >= k {
		return k
	}
	k -= dt
	i := 0
	for ; i < len(arr)-1; i++ {
		dt := arr[i+1] - arr[i] - 1
		if dt >= k {
			return arr[i] + k
		} else {
			k -= dt
		}
	}
	return arr[i] + k
}

func Test_1539(t *testing.T) {
	arr := []int{1, 2, 3, 4, 5}
	k := 5
	res := findKthPositive(arr, k)
	fmt.Println(res)
}
