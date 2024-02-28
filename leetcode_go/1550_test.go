package leetcode

import (
	"fmt"
	"testing"
)

func threeConsecutiveOdds(arr []int) bool {
	for i := 1; i < len(arr)-1; i++ {
		if arr[i-1]%2 == 1 &&
			arr[i]%2 == 1 &&
			arr[i+1]%2 == 1 {
			return true
		}
	}
	return false
}

// 双指针
func threeConsecutiveOdds2(arr []int) bool {
	l := len(arr)
	if l < 3 {
		return false
	}
	st := 0
	for ed := 0; ed < l; {
		if arr[ed]%2 != 1 {
			st = ed + 1
			ed = st
		} else {
			ed += 1
		}
		if ed-st >= 3 {
			return true
		}
	}
	return false
}

func Test_1550(t *testing.T) {
	arr := []int{1, 2, 34, 3, 4, 5, 7, 23, 12}
	res := threeConsecutiveOdds(arr)
	fmt.Println(res)
}
