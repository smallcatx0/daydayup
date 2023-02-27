package leetcode

import (
	"fmt"
	"testing"
)

func validMountainArray(arr []int) bool {
	var i = 0
	for ; i < len(arr)-1; i++ {
		if arr[i] == arr[i+1] {
			return false
		} else if arr[i] > arr[i+1] {
			break
		}
	}
	// fmt.Println(i)
	if i == 0 || i == len(arr)-1 {
		return false
	}
	for ; i < len(arr)-1; i++ {
		if arr[i] == arr[i+1] {
			return false
		} else if arr[i] < arr[i+1] {
			return false
		}
	}
	return true
}

func validMountainArray_1(arr []int) bool {
	l, r := 0, len(arr)-1
	for l < r && arr[l] < arr[l+1] {
		l += 1
	}
	for l < r && arr[r] < arr[r-1] {
		r -= 1
	}
	return l == r && l != 0 && r != len(arr)-1
}

func Test_941(t *testing.T) {
	nums := []int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
	res := validMountainArray(nums)
	fmt.Println(res)
}
